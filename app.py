import streamlit as st
import os
from urllib.parse import urlparse, parse_qs
from authlib.integrations.requests_client import OAuth2Session
from db.database import init_db, save_entry, get_entries
from agent.agent import get_agent_response

# ---------------------- ENV/SECRETS ----------------------
if st.secrets:  # Running on Streamlit Cloud
    GOOGLE_CLIENT_ID = st.secrets["GOOGLE_CLIENT_ID"]
    GOOGLE_CLIENT_SECRET = st.secrets["GOOGLE_CLIENT_SECRET"]
    OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY")
else:  # Running locally
    from dotenv import load_dotenv
    load_dotenv()
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Update redirect URI for production if needed
REDIRECT_URI = os.getenv("REDIRECT_URI", "https://consciousday-agent-by-shahzeb.streamlit.app/")

# Initialize DB
init_db()

st.set_page_config(page_title="ConsciousDay Agent", page_icon="🌅")

# ---------------------- GOOGLE OAUTH ----------------------
if "user" not in st.session_state:
    params = st.query_params if hasattr(st, "query_params") else st.experimental_get_query_params()

    if "code" not in params:
        # Step 1: Show login button
        oauth = OAuth2Session(
            GOOGLE_CLIENT_ID,
            GOOGLE_CLIENT_SECRET,
            scope="openid email profile",
            redirect_uri=REDIRECT_URI
        )
        auth_url, _ = oauth.create_authorization_url(
            "https://accounts.google.com/o/oauth2/auth"
        )
        st.title("🌅 ConsciousDay Agent")
        st.markdown(f"[🔐 Login with Google]({auth_url})")
        st.stop()

    else:
        # Step 2: Handle redirect with code → fetch token & user info
        code = params.get("code")[0] if isinstance(params.get("code"), list) else params.get("code")

        oauth = OAuth2Session(
            GOOGLE_CLIENT_ID,
            GOOGLE_CLIENT_SECRET,
            scope="openid email profile",
            redirect_uri=REDIRECT_URI
        )
        token = oauth.fetch_token(
            "https://oauth2.googleapis.com/token",
            code=code
        )

        user_info = oauth.get("https://www.googleapis.com/oauth2/v2/userinfo").json()

        # Save user in session and refresh app
        st.session_state["user"] = user_info
        st.rerun()

# ---------------------- MAIN APP ----------------------
if "user" in st.session_state:
    user = st.session_state["user"]

    # Sidebar
    st.sidebar.image(user.get("picture"), width=50)
    st.sidebar.write(f"**Welcome, {user['name']}!**")
    st.sidebar.write(user["email"])

    st.title("🌅 ConsciousDay Agent")

    # ---------------------- JOURNAL FORM ----------------------
    with st.form("journal_form"):
        journal = st.text_area("🌞 Morning Journal", height=150)
        dream = st.text_area("💭 Dream (if any)", height=100)
        intention = st.text_input("🎯 Intention of the Day")
        priorities = st.text_area("📌 Top 3 Priorities (comma-separated)")

        submitted = st.form_submit_button("✨ Generate My Reflection")

    if submitted:
        with st.spinner("Processing your inputs..."):
            response = get_agent_response(journal, intention, dream, priorities)

            # Save entry to SQLite
            save_entry(journal, intention, dream, priorities, response, response)

            st.success("✨ Reflection and Day Strategy Generated!")
            st.markdown("### 📝 Reflection & Strategy")
            st.write(response)

    # ---------------------- PAST ENTRIES ----------------------
    st.markdown("---")
    st.markdown("### 📅 View Past Entries")
    entries = get_entries()
    for e in entries:
        with st.expander(f"📅 {e[1]}"):
            st.markdown(f"**Journal:** {e[2]}")
            st.markdown(f"**Intention:** {e[3]}")
            st.markdown(f"**Dream:** {e[4]}")
            st.markdown(f"**Priorities:** {e[5]}")
            st.markdown(f"**Reflection:** {e[6]}")
            st.markdown(f"**Strategy:** {e[7]}")

else:
    st.warning("🔐 Please login with Google to use ConsciousDay Agent.") 

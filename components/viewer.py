import streamlit as st

def view_entry(entry):
    st.subheader(f"📅 {entry[1]}")
    st.markdown(f"**Journal:** {entry[2]}")
    st.markdown(f"**Intention:** {entry[3]}")
    st.markdown(f"**Dream:** {entry[4]}")
    st.markdown(f"**Priorities:** {entry[5]}")
    st.divider()
    st.markdown(f"### 🪞 Inner Reflection\n{entry[6]}")
    st.markdown(f"### 🗓 Day Strategy\n{entry[7]}")

import streamlit as st

def input_form():
    st.header("✨ Morning Reflection ✨")
    journal = st.text_area("Morning Journal")
    dream = st.text_area("Dream (optional)")
    intention = st.text_input("Intention for the Day")
    priorities = st.text_area("Top 3 Priorities (comma-separated)")
    submitted = st.button("Generate My Daily Strategy")
    return journal, dream, intention, priorities, submitted

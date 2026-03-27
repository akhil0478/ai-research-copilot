import streamlit as st
from backend.orchestrator import run_pipeline

st.title("AI Research Co-Pilot")

user_input = st.text_input("Enter Research Topic")

if st.button("Run"):
    result = run_pipeline(user_input)
    st.write(result)
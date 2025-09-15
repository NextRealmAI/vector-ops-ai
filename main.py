import streamlit as st
from agent import ComplianceAgent

st.set_page_config(page_title="Compliance Agent MVP", layout="wide")
st.title("⚖️ Compliance Agent — MVP")

uploaded_file = st.file_uploader("Upload a compliance/report PDF", type=["pdf"])

if uploaded_file:
    query = st.text_input("Ask the agent (e.g. 'What are the top compliance risks?')")

    if st.button("Analyze"):
        agent = ComplianceAgent()
        response = agent.process(uploaded_file, query)
        st.subheader("Agent Response")
        st.write(response)

# main.py (debug enhanced)

import streamlit as st
import logging
from agent import create_agent
from summarizer import summarize_pdf

# --- Logging Setup ---
logging.basicConfig(
    filename="logs/day3_debug.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

st.set_page_config(page_title="Vector Ops AI", page_icon="🛰️")

def main():
    st.title("🛰️ Vector Ops AI — Compliance Report Synthesizer")
    st.write("Upload a PDF and query compliance risks.")

    # PDF Upload
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file is not None:
        try:
            st.info("Processing PDF...")
            text_chunks = summarize_pdf(uploaded_file)
            logging.info(f"PDF processed, {len(text_chunks)} chunks created.")
            st.success("PDF processed successfully ✅")
        except Exception as e:
            st.error("❌ PDF Processing Failed. Check logs.")
            logging.exception("Error during PDF processing")
            return
    else:
        st.warning("Please upload a PDF to continue.")
        return

    # Query Input
    query = st.text_input("Enter your compliance question:")
    if query:
        try:
            agent = create_agent(text_chunks)
            logging.info("Agent created successfully.")
            response = agent.run(query)
            st.subheader("Agent Response:")
            st.write(response)
            logging.info(f"Agent response delivered for query: {query}")
        except Exception as e:
            st.error("❌ Agent execution failed. Check logs.")
            logging.exception("Error during agent execution")

if __name__ == "__main__":
    main()

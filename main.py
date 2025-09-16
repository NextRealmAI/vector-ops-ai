"""
main.py — Entry Point for Vector-Ops-AI
=======================================

CLI runner for testing the VectorOpsAgent with Gemini.
"""

import logging
from agent import VectorOpsAgent

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def main():
    logging.info("🚀 Starting VectorOps-AI with Gemini...")

    agent = VectorOpsAgent()

    try:
        # Load a sample PDF
        pdf_path = "sample.pdf"  # Replace with your test PDF
        logging.info(f"Loading PDF: {pdf_path}")
        chunks = agent.load_pdf(pdf_path)
        logging.info(f"Extracted {len(chunks)} chunks.")

        # Build embeddings
        logging.info("Building embeddings...")
        agent.build_embeddings()

        # Run a test query
        query = "Summarize the key risks in this document."
        logging.info(f"Running query: {query}")
        answer = agent.query(query)

        print("\n=== Gemini Output ===")
        print(answer)

    except Exception as e:
        logging.error(f"❌ Error occurred: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()

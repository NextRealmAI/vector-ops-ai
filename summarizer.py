"""
summarizer.py — Pure Gemini implementation for Vector-Ops-AI
============================================================

This module handles text summarization & Q&A without LangChain.
It uses Google Gemini's SDK directly for flexible document intelligence.

Author: Operative Omega-7
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ Missing GEMINI_API_KEY in environment variables.")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


def summarize_text(chunks: list[str], query: str = "Summarize this document."):
    """
    Summarize or answer questions from document chunks using Gemini.

    Args:
        chunks (list[str]): List of text chunks from a document.
        query (str): User query, e.g., "Summarize", "Extract key risks".

    Returns:
        str: AI-generated summary or answer.
    """
    model = genai.GenerativeModel("gemini-1.5-pro")

    # Build context from chunks
    context = "\n\n".join(chunks[:20])  # limit first 20 chunks for token safety

    prompt = f"""
You are an AI Document Intelligence Agent.
Context:
{context}

Task:
{query}

Rules:
- Keep output concise but informative.
- If asked for summary, provide bullet points + short abstract.
- If asked a question, cite relevant context.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini API Error: {str(e)}"


# Debugging hook
if __name__ == "__main__":
    test_chunks = [
        "This is a dummy text about AI agents revolutionizing finance.",
        "AI-driven compliance tools reduce human errors in reporting.",
    ]
    print(summarize_text(test_chunks, query="Summarize key points."))

"""
agent.py — VectorOps Agent using FAISS + Gemini Summarizer
===========================================================

Handles document ingestion, chunking, embedding, and retrieval.
Delegates summarization/Q&A to summarizer.py (Gemini).
"""

import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from summarizer import summarize_text

load_dotenv()


class VectorOpsAgent:
    def __init__(self):
        self.chunks = []
        self.vectorizer = TfidfVectorizer()
        self.embeddings = None

    def load_pdf(self, pdf_path: str):
        """Extract text from a PDF and split into chunks."""
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        self.chunks = self._chunk_text(text)
        return self.chunks

    def _chunk_text(self, text: str, chunk_size: int = 500):
        """Split text into manageable chunks."""
        words = text.split()
        return [
            " ".join(words[i:i + chunk_size])
            for i in range(0, len(words), chunk_size)
        ]

    def build_embeddings(self):
        """Create TF-IDF embeddings for chunks (lightweight vector store)."""
        if not self.chunks:
            raise ValueError("No chunks available. Load a PDF first.")
        self.embeddings = self.vectorizer.fit_transform(self.chunks)

    def query(self, user_query: str):
        """Find relevant chunks and pass them to Gemini summarizer."""
        if self.embeddings is None:
            raise ValueError("Embeddings not built. Call build_embeddings().")

        # Rank chunks by cosine similarity
        query_vec = self.vectorizer.transform([user_query])
        scores = cosine_similarity(query_vec, self.embeddings).flatten()
        top_indices = scores.argsort()[-5:][::-1]  # top 5 chunks
        top_chunks = [self.chunks[i] for i in top_indices]

        return summarize_text(top_chunks, query=user_query)

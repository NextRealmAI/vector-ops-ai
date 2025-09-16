# 🛰️ Vector-Ops-AI

**Vector-Ops-AI** is an experimental AI agent that ingests long PDF reports and produces **action-oriented summaries** using **Google Gemini**.  
Designed for banking/compliance analysts, researchers, and operators who need rapid signal extraction from dense documents.

---

## 🚀 Features
- 📂 Upload and parse PDF reports  
- 🔎 Chunk text + retrieve relevant sections with cosine similarity (TF-IDF)  
- 🤖 Summarize content using **Gemini 1.5 Pro** (`google-generativeai`)  
- 🎯 Generate concise, structured insights from dense data  

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/vector-ops-ai.git
cd vector-ops-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# Install dependencies
```bash
pip install -r requirements.txt
```

```bash

🔑 Setup

Copy .env.example to .env:

cp .env.example .env


Add your Gemini API key (from Google AI Studio):

GEMINI_API_KEY=your_api_key_here
LOG_LEVEL=INFO

🛠️ Usage

Run a query against a PDF:

python main.py --pdf ./sample_docs/report.pdf --query "What are the compliance risks?"


Example output:

[INFO] Loading PDF...
[INFO] Chunking into 12 sections...
[INFO] Running query: compliance risks
[INFO] Summarizing with Gemini...
[OUTPUT] 
1. Risk of AML non-compliance in transaction monitoring
2. Weakness in data retention policies
3. Recommendation: Update KYC processes quarterly

📂 Project Structure
vector-ops-ai/
│
├── main.py          # CLI entry point
├── agent.py         # Handles PDF ingestion + retrieval
├── summarizer.py    # Gemini summarization logic
├── requirements.txt # Dependencies
├── .env.example     # Environment variable template
└── README.md

⚡ Roadmap

 Add Streamlit/Gradio UI

 Support DOCX/HTML input

 Export summaries → Markdown/Notion

🕶️ Disclaimer

This is an experimental tool. Validate outputs before using in production compliance/legal workflows.
AI is an assistant — you are the final authority.

👤 Author

Maintained by a pseudonymous operator of Vector-Ops-AI.
Building AI agents, wealth ops, and sovereign systems.
Follow the mission logs for updates.

```

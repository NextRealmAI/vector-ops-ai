from summarizer import PDFSummarizer

class ComplianceAgent:
    def __init__(self):
        self.summarizer = PDFSummarizer()

    def process(self, pdf_file, query: str) -> str:
        """
        Orchestrates PDF processing and Q&A.
        """
        try:
            return self.summarizer.answer_question(pdf_file, query)
        except Exception as e:
            return f"⚠️ Error: {str(e)}"

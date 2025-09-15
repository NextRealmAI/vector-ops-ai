import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

class PDFSummarizer:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def answer_question(self, pdf_file, query: str) -> str:
        # Save uploaded file temporarily
        temp_path = "temp.pdf"
        with open(temp_path, "wb") as f:
            f.write(pdf_file.getbuffer())

        # Load and split
        loader = PyPDFLoader(temp_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)

        # Vector store
        vectorstore = FAISS.from_documents(chunks, self.embeddings)
        retriever = vectorstore.as_retriever()

        # Conversational chain
        qa_chain = ConversationalRetrievalChain.from_llm(self.llm, retriever)
        result = qa_chain.run(query)

        return result

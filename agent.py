import google.generativeai as genai

genai.configure(api_key="your_key_here")

def create_agent(text_chunks):
    model = genai.GenerativeModel("gemini-1.5-pro")
    def run(query):
        prompt = f"Context:\n{text_chunks}\n\nQuestion: {query}"
        response = model.generate_content(prompt)
        return response.text
    return type("Agent", (), {"run": run})()

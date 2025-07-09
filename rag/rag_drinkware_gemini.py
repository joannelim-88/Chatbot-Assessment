#RAG integration for drinkware (FAISS)

#Import libraries
import faiss
import numpy as np
from dotenv import load_dotenv
import os 
import google.generativeai as genai


#Load model
load_dotenv()
client = genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
    )

#Functions 
def load_doc(filepath="data/zus-drinkware.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
    
def get_embedding(text):
    model = "models/embedding-001"
    return genai.embed_content(
        model=model,
        content=text,
        task_type="retrieval_document"  
    )["embedding"]

def build_faiss_index():
    document = load_doc()
    embedding = [get_embedding(doc) for doc in document]
    dim = len(embedding[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embedding).astype("float32"))

    return index, document

def search(query, index, document, k=3):
    query_embedding = np.array([get_embedding(query)]).astype("float32")
    D, I = index.search(query_embedding, k)
    return [document[i] for i in I[0]]

def generate_summary(query, top_docs):
    context = "\n".join(top_docs)
    prompt = f"""
Summarize most relevant drinkware options based on user question input:
User's question: {query}
Documents: {context}
Provide a concise summary"""
    
    model= genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

#To test query 
#Simply type http://localhost:8000/products?query=travel+mug and put on browser to view results



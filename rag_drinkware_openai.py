#RAG integration for drinkware (FAISS)

#Import libraries
import faiss
import numpy as np
from dotenv import load_dotenv
import os 
from openai import OpenAI

#Load openai 
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

#Functions 
def load_doc(filepath="data/zus-drinkware.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
    
def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

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
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":prompt}]
    )
    return response.choices[0].message.content

#To test query 
#Simply type http://localhost:8000/products?query=travel+mug and put on browser to view results

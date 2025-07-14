
from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import faiss
from huggingface_hub import hf_hub_download


app = FastAPI(title="Reccomender API")  # Create the app instance


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # <-- allow frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


REPO_ID = "Ra-Ma-Dan/recomend.er"
# Global variables to hold loaded data
index = None
embeddings = None
news_df = None


@app.on_event("startup")
def load_assets():
    global index, embeddings, df, model
    
    #Loading the Model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    # Download and load FAISS index
    index_path = hf_hub_download(repo_id=REPO_ID, filename="faiss_index.index")
    index = faiss.read_index(index_path)

    # Load embeddings
    embeddings_path = hf_hub_download(repo_id=REPO_ID, filename="embedded_titles.npy")
    embeddings = np.load(embeddings_path)

    # Load CSV
    csv_path = hf_hub_download(repo_id=REPO_ID, filename="news_data.csv")
    df = pd.read_csv(csv_path)

    print("✅ All files loaded successfully.")



user_interest = []

class Query(BaseModel):
    interests: Optional[List[str]] = None
    top_k: int = 5

@app.post("/recommend")    
def recommend(query: Query):
    if not query.interests:
        query.interests = ["Religion", "musical world", "Technology"]
        
    finall_recommendation = []
    for interest in query.interests:
        interest_embedding = model.encode([interest], convert_to_numpy=True).astype("float32")
    # similarity = cosine_similarity(interest_embedding, embeddings)
    # top_indices = similarity.argsort()[0][-query.top_k:][::-1]
        faiss.normalize_L2(interest_embedding)
    
        distances, indices = index.search(interest_embedding, query.top_k)
    
        interest_results = []
        for idx, score in zip(indices[0], distances[0]):
            interest_results.append({
                "id": (df.iloc[idx]["news_id"]),
                "text": df.iloc[idx]["title"],
                "url": df.iloc[idx]["url"],
                "category": df.iloc[idx]["category"],
                "score": float(score)
            })
        
        finall_recommendation.append({
            "interset" : interest,
            "recommedations" : interest_results
        })
    return  {
        "Interests": query.interests,
        "recommendations": finall_recommendation
    }
    
    


# GET endpoint (e.g. to test the API)
@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

# POST endpoint to receive data
@app.post("/items/")
def create_item(item: str):
    return {"received_item": item}

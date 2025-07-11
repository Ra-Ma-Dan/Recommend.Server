# Recommend.Server

# 🧠 Recc.er - FastAPI Recommendation API

This project is a lightweight recommendation system built with **FastAPI**, **FAISS**, and **Hugging Face**. It lets users input a query (e.g., "tech") and receive a list of similar news articles based on sentence embeddings.

---

## 🚀 Features

- ✅ Sentence-based similarity search using `sentence-transformers`
- ✅ Fast similarity search using FAISS index
- ✅ Embeddings and data are hosted on Hugging Face
- ✅ Deployed with Render (zero-downtime API hosting)

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```
.
├── app/
│   └── main.py           # FastAPI app logic
├── start.sh              # Startup script for Render
├── requirements.txt      # Python dependencies
└── README.md



******************* API Endpoints
GET /
Returns a welcome message.

GET /recommend/?query=...
Takes a query array of string(s) and returns the top 5 most similar news articles.

####################  Example:

```bash
GET /recommend/?query=climate change
```

#####################  Response:
{
  "results": [
    {
      "title": "Climate action heats up...",
      "url": "...",
      "abstract": "..."
    },
    ...
  ]
}


############   Deployment (Render)

Connect this repo to https://render.com

Set build command:

```bash
pip install -r requirements.txt
Set start command:
```


```bash
./start.sh
```

Deploy as a Web Service

📥 Data Hosting
All model files are hosted on Hugging Face under:

🔗 Ra-Ma-Dan/Recommender.er

These include:

faiss.index – FAISS vector index

embedded_titles.npy – Sentence-transformer embeddings

news_data.csv – Original news article metadata from MIND

🧠 Embedding Model Used
sentence-transformers/all-MiniLM-L6-v2

📬 Contact
For help or questions, open an issue or contact @Ra-Ma-Dan

📜 License
MIT License – free for personal and commercial use.


## 🪄 Bonus Tips

- You can include a **live Render link** once deployed:  
  `https://reccer-api.onrender.com`


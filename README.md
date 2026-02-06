# 🎬 Movie Recommendation System (ML + FastAPI + React)

A full-stack Movie Recommendation System built using Machine Learning, FastAPI, and React.
The system recommends similar movies based on content similarity using TF-IDF vectorization and cosine similarity, with intelligent search powered by RapidFuzz for handling typos and partial matches.

---

## 🚀 Features

- Content-based movie recommendation system
- FastAPI backend with REST API
- React frontend with modern UI
- Movie poster integration using TMDB API
- Intelligent search (case insensitive & typo tolerant)
- Partial movie matching (avenger → The Avengers)
- Auto suggestions while typing
- Handles invalid movie inputs gracefully
- Clean modular architecture

---

## 🧠 Machine Learning Approach

The recommendation engine is built using:
- TF-IDF Vectorization on movie metadata
- Cosine Similarity for similarity scoring
- Precomputed similarity matrix for fast recommendations
- RapidFuzz for fuzzy string matching

## Workflow

- Movie metadata is processed.
- TF-IDF vectors are created.
- Cosine similarity is calculated.
- Top similar movies are returned.
- Poster URLs are fetched dynamically.

## 🏗️ Project Architecture
 
```text
Movie-Recommendation-System/
│
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI entry point
│   │   ├── recommender.py         # Recommendation logic
│   │   ├── utils.py               # Helper functions (poster fetch, etc.)
│   │   └── __pycache__/
│   │
│   └── artifacts/
│       └── model/
│           ├── df.pkl             # Processed movie dataframe
│           ├── indices.pkl        # Movie index mapping
│           ├── tfidf.pkl          # TF-IDF vectorizer
│           └── tfidf_matrix.pkl   # TF-IDF matrix
│
├── data/
│   └── raw/
│       ├── tmdb_5000_movies.csv
│       └── tmdb_5000_credits.csv
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   │   └── api.js             # Backend API calls
│   │   ├── components/
│   │   │   └── MovieCard.js       # Movie display component
│   │   ├── pages/
│   │   │   └── Home.js            # Main UI page
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── styles.css
│   │   └── index.js
│   │
│   ├── package.json
│   └── package-lock.json
│
├── Notebook/
│   └── EDA.ipynb                  # Data exploration & experimentation
│
├── src/
│   └── pipelines/
│       ├── model.py               # Model creation pipeline
│       └── __init__.py
│
├── requirements.txt               # Python dependencies
└── README.md
```

## 🧩 Tech Stack

## Backend
- Python
- FastAPI
- Scikit-learn
- Pandas
- RapidFuzz

##  Frontend
- React.js
- Axios
- CSS
- Machine Learning
- TF-IDF Vectorizer
- Cosine Similarity

## Machine Learning

- TF-IDF Vectorizer
- Cosine Similarity

## 👨‍💻 Author

Ramakrishna Tagore

Machine Learning & Data Scientist
Passionate about AI, ML systems, and scalable backend applications.
import os
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process, fuzz
from app.utils import fetch_poster

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "model")
DF_PATH = os.path.join(MODEL_PATH, "df.pkl")

with open(os.path.join(MODEL_PATH, "tfidf.pkl"), "rb") as f:
    tfidf = pickle.load(f)

with open(os.path.join(MODEL_PATH, "tfidf_matrix.pkl"), "rb") as f:
    tfidf_matrix = pickle.load(f)

with open(os.path.join(MODEL_PATH, "indices.pkl"), "rb") as f:
    indices = pickle.load(f)

movies_df = pd.read_pickle(DF_PATH)

movie_titles = list(indices.index)
movie_titles_lower = [m.lower() for m in movie_titles]


def find_closest_title(user_input: str):
    user_input = user_input.lower()

    match = process.extractOne(
        user_input,
        movie_titles_lower,
        scorer=fuzz.WRatio
    )

    if match and match[1] >= 60:
        return movie_titles[movie_titles_lower.index(match[0])]

    return None


def fetch_poster_by_title(title: str):
    row = movies_df[movies_df['title'] == title]
    if row.empty:
        return None

    movie_id = int(row['movie_id'].values[0])
    return fetch_poster(movie_id)


def get_recommendations(title: str, n: int = 12):

    matched_title = find_closest_title(title)

    if not matched_title:
        return {
            "movie": title,
            "recommendations": []
        }

    idx = indices[matched_title]

    sim_scores = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    similar_indices = sim_scores.argsort()[::-1][1:n+1]

    results = []

    for i in similar_indices:
        movie_title = indices.index[i]
        results.append({
            "title": movie_title,
            "poster": fetch_poster_by_title(movie_title)
        })

    return {
        "movie": matched_title,
        "recommendations": results
    }

import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../../data/processed/df.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "../../artifacts/model")

class MovieRecommender:
    def __init__(self):
        self.df = pd.read_pickle(DATA_PATH)
        with open(os.path.join(MODEL_PATH, "tfidf.pkl"), "rb") as f:
            self.tfidf = pickle.load(f)
        with open(os.path.join(MODEL_PATH, "tfidf_matrix.pkl"), "rb") as f:
            self.tfidf_matrix = pickle.load(f)
        with open(os.path.join(MODEL_PATH, "indices.pkl"), "rb") as f:
            self.indices = pickle.load(f)

    def _get_closest_title(self, title: str):
        closest = process.extractOne(title, self.df['title'].tolist())
        return closest[0] if closest else title

    def recommend(self, title: str):
        N = 6
        title = self._get_closest_title(title)
        if title not in self.indices:
            return ["Movie not found"]
        idx = self.indices[title]
        sim_score = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()
        similar_idx = sim_score.argsort()[::-1][1:N+1]
        return self.df['title'].iloc[similar_idx]

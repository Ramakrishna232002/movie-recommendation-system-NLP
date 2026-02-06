from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.recommender import get_recommendations

app = FastAPI(title="Movie Recommendation API")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommend")
def recommend(movie: str):
    """
    GET /recommend?movie=MovieName
    Returns top 5 recommended movies with posters
    """
    return get_recommendations(movie)

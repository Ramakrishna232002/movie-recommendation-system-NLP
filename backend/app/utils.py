import requests

# 🔑 TMDB API key
TMDB_API_KEY = "c9cdd5fe47785a34e52a8c0458d01b32"
TMDB_BASE_URL = "https://api.themoviedb.org/3/movie/"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

def fetch_poster(movie_id: int):
    """
    Given a movie_id, return full poster URL from TMDB.
    Returns None if movie not found or no poster.
    """
    try:
        url = f"{TMDB_BASE_URL}{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return TMDB_IMAGE_URL + poster_path
        return None
    except requests.exceptions.RequestException:
        return None

import React, { useState } from "react";
import { getRecommendations } from "../api/api";
import MovieCard from "../components/MovieCard";
import { FaSearch } from "react-icons/fa";

function Home() {
  const [movie, setMovie] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleRecommend = async () => {
    if (!movie) return;

    setLoading(true);
    setError("");
    setRecommendations([]);

    try {
      const data = await getRecommendations(movie);

      if (!data.recommendations.length) {
        setError("No such movie exists.");
      } else {
        setRecommendations(data.recommendations);
      }
    } catch {
      setError("No such movie exists.");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🎬 Movie Recommender</h1>

      <div className="search-box">
        <FaSearch className="search-icon" />
        <input
          type="text"
          placeholder="Type movie name..."
          value={movie}
          onChange={(e) => setMovie(e.target.value)}
        />
        <button onClick={handleRecommend}>
          Recommend
        </button>
      </div>

      {loading && <p className="loading">Finding movies...</p>}
      {error && <p className="error">{error}</p>}

      <div className="movie-grid">
        {recommendations.map((movie, index) => (
          <MovieCard
            key={index}
            title={movie.title}
            poster={movie.poster}
          />
        ))}
      </div>
    </div>
  );
}

export default Home;

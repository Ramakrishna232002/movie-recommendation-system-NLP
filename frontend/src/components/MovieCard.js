import React from "react";
import { FaFilm } from "react-icons/fa";

function MovieCard({ title, poster }) {
  return (
    <div className="movie-card">
      <img src={poster} alt={title} />
      <div className="movie-title">
        <FaFilm className="icon" />
        <span>{title}</span>
      </div>
    </div>
  );
}

export default MovieCard;

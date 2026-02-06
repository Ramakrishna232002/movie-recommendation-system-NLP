const BASE_URL = "http://127.0.0.1:8000";

export const getRecommendations = async (movie) => {
  const response = await fetch(
    `${BASE_URL}/recommend?movie=${encodeURIComponent(movie)}`
  );

  if (!response.ok) {
    throw new Error("Movie not found");
  }

  return await response.json();
};

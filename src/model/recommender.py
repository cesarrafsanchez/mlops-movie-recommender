import pickle
from pathlib import Path


class MovieRecommender:
    def __init__(self):
        # Cargamos los archivos al iniciar la clase
        # Usamos Path para evitar problemas de rutas entre Windows/Linux
        current_path = Path(__file__).parent

        with open(current_path / 'movie_titles.pkl', 'rb') as f:
            self.titles = pickle.load(f)

        with open(current_path / 'corr_matrix.pkl', 'rb') as f:
            self.corr_matrix = pickle.load(f)

    def get_recommendations(self, movie_title, top_n=10):
        # Lógica de búsqueda flexible
        if movie_title not in self.titles:
            matches = [t for t in self.titles if movie_title.lower() in t.lower()]
            if not matches:
                return {"error": "Película no encontrada", "recommendations": []}
            movie_title = matches[0]  # Tomamos la mejor coincidencia

        # Lógica de recomendación (la misma que tenías antes)
        movie_idx = self.titles.index(movie_title)
        corr_movie = self.corr_matrix[movie_idx]

        # Crear lista de tuplas (titulo, score)
        rec_list = list(zip(self.titles, corr_movie))

        # Ordenar y filtrar
        rec_list.sort(key=lambda x: x[1], reverse=True)

        # Devolvemos solo los títulos y sus scores, excluyendo el primero (ella misma)
        results = rec_list[1:top_n + 1]

        return {
            "query_movie": movie_title,
            "recommendations": [{"title": r[0], "score": round(r[1], 4)} for r in results]
        }


# Bloque de prueba: Solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    recommender = MovieRecommender()
    print(recommender.get_recommendations("Matrix"))
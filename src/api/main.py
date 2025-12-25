import sys
import os

# --- HACK DE RUTAS ---
# Añadimos la carpeta raíz del proyecto al sistema para poder importar 'src'
# Esto soluciona el error clásico "ModuleNotFoundError"
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import FastAPI, HTTPException
from src.model.recommender import MovieRecommender

# Inicializamos la aplicación
app = FastAPI(
    title="CinemaRecSys API",
    description="API de recomendación de películas basada en SVD y Filtrado Colaborativo",
    version="1.0.0"
)

# --- CARGA DEL MODELO (SINGLETON PATTERN) ---
# Instanciamos la clase UNA sola vez al arrancar el servidor.
# Si lo hiciéramos dentro de la función de recomendación, cargaríamos los archivos
# en cada petición, lo que haría la API lentísima.
recommender = MovieRecommender()


@app.get("/")
def read_root():
    return {"message": "Bienvenido a CinemaRecSys API. Visita /docs para probar."}


@app.get("/recommend/{movie_title}")
def get_recommendations(movie_title: str):
    """
    Endpoint principal. Recibe un título y devuelve recomendaciones.
    """
    result = recommender.get_recommendations(movie_title)

    # Manejo de errores básicos
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result
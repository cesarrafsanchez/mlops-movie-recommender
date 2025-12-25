import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import TruncatedSVD
from pathlib import Path

# Configuración de Rutas
# __file__ es este archivo (train.py).
# .parent es src/model
# .parent.parent es src
# .parent.parent.parent es la raíz del proyecto
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / 'data'
MODEL_DIR = BASE_DIR / 'src' / 'model'


def train_model():
    print("🚀 Iniciando proceso de entrenamiento...")

    # 1. Cargar Datos
    ratings_file = DATA_DIR / 'ratings.csv'
    movies_file = DATA_DIR / 'movies.csv'

    if not ratings_file.exists() or not movies_file.exists():
        raise FileNotFoundError(f"No se encontraron los archivos en {DATA_DIR}. Asegúrate de descargar MovieLens.")

    print("   ...Cargando datasets")
    ratings = pd.read_csv(ratings_file)
    movies = pd.read_csv(movies_file)

    # 2. Preprocesamiento (Merge y Pivot)
    print("   ...Creando matriz de utilidad (User-Item)")
    df = pd.merge(ratings, movies, on='movieId', how='inner')
    matrix = df.pivot_table(index='title', columns='userId', values='rating').fillna(0)

    # 3. Entrenamiento (SVD)
    print("   ...Entrenando modelo SVD (Reducción de dimensionalidad)")
    # Usamos 12 componentes como definimos en el notebook
    SVD = TruncatedSVD(n_components=12, random_state=42)
    matrix_reduced = SVD.fit_transform(matrix)

    # 4. Cálculo de Correlaciones
    print("   ...Calculando matriz de correlación de Pearson")
    corr_matrix = np.corrcoef(matrix_reduced)

    # 5. Guardar Artefactos
    print("💾 Guardando modelo y artefactos...")

    # Guardamos la lista de títulos (para mapear índices)
    titles = list(matrix.index)
    with open(MODEL_DIR / 'movie_titles.pkl', 'wb') as f:
        pickle.dump(titles, f)

    # Guardamos la matriz de correlación
    with open(MODEL_DIR / 'corr_matrix.pkl', 'wb') as f:
        pickle.dump(corr_matrix, f)

    print(f"✅ ¡Entrenamiento finalizado! Archivos guardados en: {MODEL_DIR}")


if __name__ == "__main__":
    train_model()
# 🎬 CinemaRecSys: Machine Learning Movie Recommender

Un sistema de recomendación **End-to-End** capaz de sugerir películas basado en filtrado colaborativo (SVD). El proyecto expone el modelo a través de una API RESTful de alto rendimiento y está totalmente contenerizado con Docker.

---

## 🚀 Características

* **Motor de IA:** Filtrado Colaborativo usando *Singular Value Decomposition* (SVD).
* **API Robusta:** Construida con **FastAPI** (validación de datos y documentación automática).
* **Búsqueda Inteligente:** Algoritmo de coincidencia difusa (*Fuzzy Matching*) para títulos mal escritos.
* **Portable:** Despliegue inmediato mediante **Docker** con entrenamiento automático en el build.

---

## 🛠️ Tech Stack

* **Lenguaje:** Python 3.11
* **ML Libraries:** Scikit-Learn, Pandas, Numpy.
* **Backend:** FastAPI, Uvicorn.
* **DevOps:** Docker (con optimización de capas).

---

## 📦 Cómo ejecutar (Docker)

Esta es la forma recomendada, ya que Docker se encarga de entrenar el modelo y configurar las dependencias automáticamente.

1.  **Construir la imagen:**
    ```bash
    docker build -t cinema-recsys .
    ```

2.  **Correr el contenedor:**
    ```bash
    docker run -p 8000:8000 cinema-recsys
    ```

3.  **Probar la API:**
    Abre tu navegador en `http://localhost:8000/docs` para acceder a la interfaz interactiva de Swagger y probar el endpoint `/recommend`.

---

## 🔧 Instalación Local (Entorno de Desarrollo)

Si deseas modificar el código o realizar un análisis exploratorio de datos (EDA) en tu máquina local:

1.  **Clonar el repositorio.**
2.  **Crear y activar el entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4.  **Entrenar el modelo:**
    Es necesario ejecutar este paso manualmente para generar los archivos `.pkl` pesados (que no se suben al repositorio por límites de tamaño de GitHub).
    ```bash
    python src/model/train.py
    ```
5.  **Ejecutar la API:**
   ```bash
    uvicorn src.api.main:app --reload
    ```

---

## 📂 Estructura del Proyecto

```plaintext
├── data/               # Dataset (MovieLens: movies.csv, ratings.csv)
├── src/
│   ├── api/            # Endpoints de FastAPI y lógica de la API
│   └── model/          # Script de entrenamiento y almacenamiento de modelos (.pkl)
├── notebooks/          # Jupyter Notebooks para EDA y prototipado
├── Dockerfile          # Configuración de imagen con entrenamiento integrado
├── .dockerignore       # Exclusión de venv y archivos pesados para el build
└── requirements.txt    # Dependencias del proyecto


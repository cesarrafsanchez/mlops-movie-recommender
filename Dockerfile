# 1. Imagen base: Usamos una versión ligera de Python (Slim)
# Esto es como elegir el sistema operativo de nuestra "caja"
FROM python:3.11-slim

# 2. Directorio de trabajo: Creamos una carpeta dentro del contenedor
WORKDIR /app

# 3. Copiar dependencias: Primero copiamos solo el requirements.txt
# (Esto es un truco de caché para que las builds sean más rápidas)
COPY requirements.txt .

# 4. Instalar librerías: Le decimos a pip que instale todo
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código fuente:
# Copiamos la carpeta src (que incluye tu modelo .pkl y la API) al contenedor
COPY src/ ./src/

# 6. Exponer el puerto: Avisamos que la app escuchará en el puerto 8000
EXPOSE 8000

# 7. El comando de arranque:
# --host 0.0.0.0 es CRUCIAL en Docker (significa "escucha desde fuera del contenedor")
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
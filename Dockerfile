# Imagen base ligera de Python
FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero requirements para aprovechar cache de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Puerto que usará gunicorn (Render inyecta la variable PORT automáticamente)
EXPOSE 10000

# Comando de arranque. Render define $PORT; si no existe, usamos 10000 como respaldo
CMD gunicorn --bind 0.0.0.0:${PORT:-10000} app:app
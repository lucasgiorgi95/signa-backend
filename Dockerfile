# Usar una imagen base de Python 3.13
FROM python:3.13-slim

# Instalar dependencias del sistema incluyendo SQLite
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio para la aplicación
RUN mkdir -p /app

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY . .

# Crear directorio de datos con permisos amplios
RUN mkdir -p /app/data && \
    chmod -R 777 /app/data

# Hacer que el script sea ejecutable
RUN chmod +x /app/start.sh

# Puerto expuesto
EXPOSE 8000

# Usar el usuario por defecto de Render (no-root)
USER 1000

# Comando para ejecutar la aplicación
CMD ["/app/start.sh"]

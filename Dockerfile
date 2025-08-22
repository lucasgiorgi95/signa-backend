# Usar una imagen base de Python 3.13
FROM python:3.13-slim

# Instalar dependencias del sistema incluyendo SQLite
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio para la aplicación y dar permisos
RUN mkdir -p /app/data && \
    chmod 777 /app && \
    chmod 777 /app/data

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY . .

# Puerto expuesto
EXPOSE 8000

# Cambiar permisos del script de inicio
RUN chmod +x /app/start.sh

# Usar un usuario no-root (1000 es el usuario por defecto en Render)
USER 1000

# Comando para ejecutar la aplicación
CMD ["/app/start.sh"]

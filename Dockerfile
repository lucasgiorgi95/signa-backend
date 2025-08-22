# Usar una imagen base de Python 3.13
FROM python:3.13-slim

# Instalar dependencias del sistema incluyendo SQLite
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio para la aplicación
RUN mkdir -p /app/data

# Establecer el directorio de trabajo
WORKDIR /app

# Crear un usuario no-root para mayor seguridad
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copiar los archivos necesarios
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY . .

# Dar permisos al directorio de datos
RUN chown -R appuser:appuser /app/data

# Cambiar al usuario no-root
USER appuser

# Puerto expuesto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["sh", "start.sh"]

#!/bin/bash
# Iniciar la aplicación

# Crear la base de datos si no existe
if [ ! -f "/app/marcas.db" ]; then
    echo "Creando base de datos SQLite..."
    sqlite3 /app/marcas.db ""
    # Aquí podrías agregar comandos para inicializar la base de datos
    # por ejemplo: sqlite3 /app/marcas.db < /app/init_db.sql
fi

echo "Iniciando la aplicación en el puerto $PORT..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1

#!/bin/bash

# Crear directorio de datos si no existe
mkdir -p /app/data

# Ruta completa a la base de datos
DB_PATH="/app/data/marcas.db"

# Crear la base de datos si no existe
if [ ! -f "$DB_PATH" ]; then
    echo "Creando base de datos SQLite en $DB_PATH..."
    touch "$DB_PATH"
    chmod 666 "$DB_PATH"
    
    # Inicializar la base de datos con SQLite
    sqlite3 "$DB_PATH" ""
    
    # Aquí podrías agregar comandos para inicializar la base de datos
    # por ejemplo: sqlite3 "$DB_PATH" < /app/init_db.sql
    
    echo "Base de datos creada correctamente"
fi

# Exportar la ruta de la base de datos para que la aplicación la use
export DATABASE_URL="sqlite:////app/data/marcas.db"

echo "Iniciando la aplicación en el puerto ${PORT:-8000}..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1

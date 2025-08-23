#!/bin/bash

echo "Iniciando aplicación..."

# Mostrar información de la base de datos (sin mostrar credenciales completas)
if [[ "$DATABASE_URL" == *"postgresql"* ]]; then
    echo "Usando PostgreSQL"
elif [[ "$DATABASE_URL" == *"sqlite"* ]]; then
    echo "Usando SQLite"
else
    echo "Tipo de base de datos no reconocido"
fi

# Ejecutar la aplicación
echo "Iniciando servidor en puerto ${PORT:-8000}..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1

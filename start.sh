#!/bin/bash
# Iniciar la aplicación
echo "Iniciando la aplicación en el puerto $PORT..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1

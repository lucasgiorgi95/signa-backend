#!/bin/bash
# Iniciar la aplicación
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT

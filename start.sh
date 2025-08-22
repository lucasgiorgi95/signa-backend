#!/bin/bash

# Configuración de rutas
APP_DIR="/app"
DATA_DIR="/data"  # Directorio montado por Render
DB_PATH="$DATA_DIR/marcas.db"

# Verificar que el directorio de datos esté disponible
echo "Verificando directorio de datos en $DATA_DIR..."

# Esperar a que el directorio esté disponible (Render lo monta automáticamente)
if [ ! -d "$DATA_DIR" ]; then
    echo "Esperando a que Render monte el directorio de datos..."
    sleep 2
fi

# Verificar nuevamente
if [ ! -d "$DATA_DIR" ]; then
    echo "ADVERTENCIA: Directorio de datos no disponible, usando directorio local"
    DATA_DIR="/app/data"
    DB_PATH="$DATA_DIR/marcas.db"
    mkdir -p "$DATA_DIR"
fi

echo "Usando directorio de datos: $DATA_DIR"

# Crear la base de datos si no existe
if [ ! -f "$DB_PATH" ]; then
    echo "Creando base de datos SQLite en $DB_PATH..."
    
    # Crear archivo vacío
    touch "$DB_PATH"
    
    # Verificar si se creó el archivo
    if [ $? -ne 0 ]; then
        echo "ERROR: No se pudo crear el archivo de la base de datos"
        ls -la "$DATA_DIR"
        exit 1
    fi
    
    # Establecer permisos
    chmod 666 "$DB_PATH"
    
    # Inicializar la base de datos
    if ! sqlite3 "$DB_PATH" ""; then
        echo "ERROR: No se pudo inicializar la base de datos"
        ls -la "$DATA_DIR"
        exit 1
    fi
    
    echo "Base de datos creada correctamente"
fi

# Verificar permisos
echo "Verificando permisos..."
ls -la "$DATA_DIR"

# Configurar la variable de entorno para la URL de la base de datos
if [ -z "$DATABASE_URL" ]; then
    export DATABASE_URL="sqlite:///$DB_PATH"
fi

echo "Usando DATABASE_URL: $DATABASE_URL"

echo "Iniciando la aplicación en el puerto ${PORT:-8000}..."

# Ejecutar la aplicación
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1

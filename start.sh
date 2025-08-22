#!/bin/bash

# Configuración de rutas
APP_DIR="/app"
DATA_DIR="/data"  # Cambiado a /data para coincidir con render.yaml
DB_PATH="$DATA_DIR/marcas.db"

# Verificar y crear directorio de datos con permisos
echo "Configurando directorio de datos en $DATA_DIR..."

# Crear directorio de datos si no existe
if [ ! -d "$DATA_DIR" ]; then
    mkdir -p "$DATA_DIR"
    chmod -R 777 "$DATA_DIR"
    
    # Verificar si se creó correctamente
    if [ $? -ne 0 ]; then
        echo "ERROR: No se pudo crear el directorio de datos en $DATA_DIR"
        exit 1
    fi
    
    echo "Directorio de datos creado correctamente"
else
    echo "El directorio de datos ya existe"
fi

# Verificar permisos
chmod -R 777 "$DATA_DIR"

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

# Usar la variable de entorno para la URL de la base de datos
export DATABASE_URL="sqlite://$DB_PATH"

echo "Iniciando la aplicación en el puerto ${PORT:-8000}..."

# Ejecutar la aplicación
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1

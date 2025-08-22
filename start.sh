#!/bin/bash

# Configurar la ruta de la base de datos
DB_DIR="/app/data"
DB_PATH="$DB_DIR/marcas.db"

# Crear directorio de datos con permisos amplios
mkdir -p "$DB_DIR"
chmod 777 "$DB_DIR"

# Crear la base de datos si no existe
if [ ! -f "$DB_PATH" ]; then
    echo "Creando base de datos SQLite en $DB_PATH..."
    # Crear archivo vacío con permisos de escritura
    touch "$DB_PATH"
    chmod 666 "$DB_PATH"
    
    # Inicializar la base de datos con SQLite
    sqlite3 "$DB_PATH" ""
    
    if [ $? -ne 0 ]; then
        echo "Error al crear la base de datos"
        ls -la "$DB_DIR"
        exit 1
    fi
    
    echo "Base de datos creada correctamente"
fi

# Verificar permisos
echo "Verificando permisos..."
ls -la "$DB_DIR"

# Usar la variable de entorno para la URL de la base de datos
export DATABASE_URL="sqlite:///$DB_PATH"

echo "Iniciando la aplicación en el puerto ${PORT:-8000}..."

# Ejecutar la aplicación con el comando directo
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1

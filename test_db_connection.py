#!/usr/bin/env python3
"""
Script para probar la conexión a la base de datos
Úsalo localmente o en Render para verificar que todo funciona
"""

import os
from app.database import engine, SQLALCHEMY_DATABASE_URL

def test_connection():
    print(f"DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")
    
    try:
        # Probar conexión
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            print("✅ Conexión exitosa a la base de datos")
            
            # Verificar si es PostgreSQL o SQLite
            if "postgresql" in SQLALCHEMY_DATABASE_URL:
                print("🐘 Usando PostgreSQL")
            elif "sqlite" in SQLALCHEMY_DATABASE_URL:
                print("📁 Usando SQLite")
                
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    test_connection()
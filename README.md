# API de Registro de Marcas

Este es un backend desarrollado con FastAPI y SQLite para el registro y gestión de marcas comerciales.

## Características

- CRUD completo para marcas (Crear, Leer, Actualizar, Eliminar)
- Base de datos SQLite para almacenamiento persistente
- Documentación automática con Swagger UI y ReDoc
- Validación de datos con Pydantic
- Estructura modular y escalable

## Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # En Windows
   source venv/bin/activate  # En macOS/Linux
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
python run.py
```

El servidor estará disponible en `http://localhost:8000`

## Documentación de la API

- **Swagger UI (Interactivo):** http://localhost:8000/api/v1/docs
- **ReDoc (Documentación alternativa):** http://localhost:8000/api/v1/redoc

## Endpoints disponibles

### Marcas

- `GET /api/v1/marcas/` - Lista todas las marcas
- `POST /api/v1/marcas/` - Crea una nueva marca
- `GET /api/v1/marcas/{id}` - Obtiene una marca por ID
- `PUT /api/v1/marcas/{id}` - Actualiza una marca existente
- `DELETE /api/v1/marcas/{id}` - Elimina una marca

## Estructura del Proyecto

```
signa-prueba-backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # Punto de entrada de la aplicación
│   ├── database.py       # Configuración de la base de datos
│   ├── models/           # Modelos de datos
│   │   └── marca.py
│   ├── schemas/          # Esquemas Pydantic
│   │   └── marca.py
│   └── api/              # Rutas/endpoints
│       ├── __init__.py
│       └── v1/           # Versión 1 de la API
│           ├── __init__.py
│           ├── endpoints/ 
│           │   └── marcas.py
│           └── api.py    # Router principal de la API v1
├── requirements.txt      # Dependencias del proyecto
└── run.py               # Script para ejecutar la aplicación
```

## Base de Datos

La aplicación utiliza SQLite y crea automáticamente la base de datos `marcas.db` en el directorio raíz del proyecto la primera vez que se inicia la aplicación.

## Licencia

Este proyecto está bajo la Licencia MIT.
# signa-backend

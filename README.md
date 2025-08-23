# API de Registro de Marcas

Este es un backend desarrollado con FastAPI y SQLite para el registro y gestión de marcas comerciales.

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para control de versiones)

### Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/signa-backend.git
   cd signa-backend
   ```

2. Crea y activa un entorno virtual:

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

#### Usando el script run.py

```bash
python run.py
```

El servidor estará disponible en `http://localhost:8000`

#### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

## Características

- CRUD completo para marcas (Crear, Leer, Actualizar, Eliminar)
- Base de datos SQLite para almacenamiento persistente
- Documentación automática con Swagger UI y ReDoc
- Validación de datos con Pydantic
- Estructura modular y escalable

## 🏗️ Estructura del Proyecto

```
signa-prueba-backend/
├── .env.example           # Plantilla de variables de entorno
├── .gitignore             # Archivos ignorados por Git
├── Procfile               # Configuración para despliegue en Railway
├── requirements.txt       # Dependencias del proyecto
├── runtime.txt            # Versión de Python para producción
└── app/                   # Código fuente de la aplicación
    ├── __init__.py
    ├── main.py           # Punto de entrada de la aplicación
    ├── database.py       # Configuración de la base de datos
    ├── models/           # Modelos de SQLAlchemy
    │   ├── __init__.py
    │   └── marca.py      # Modelo de Marca
    ├── schemas/          # Esquemas Pydantic
    │   ├── __init__.py
    │   └── marca.py      # Esquemas para validación de datos
    └── api/              # Rutas y controladores
        ├── __init__.py
        └── v1/           # API Versión 1
            ├── __init__.py
            ├── api.py    # Router principal
            └── endpoints/
                ├── __init__.py
                └── marcas.py  # Endpoints de Marcas
```

### Componentes Principales

- **app/main.py**: Configuración principal de FastAPI y middleware CORS
- **app/database.py**: Configuración de la conexión a la base de datos
- **app/models/**: Modelos de SQLAlchemy
- **app/schemas/**: Esquemas Pydantic para validación de datos
- **app/api/v1/**: Implementación de los endpoints de la API

## 🛠️ Desarrollo

### Variables de Entorno

Crea un archivo `.env` basado en `.env.example` con las siguientes variables:

```
HOST=0.0.0.0
PORT=8000
DEBUG=True
DATABASE_URL=sqlite:///./marcas.db
```

### Formateo de Código

El proyecto utiliza `black` para formateo de código:

```bash
# Instalar black
pip install black

# Formatear código
black .
```

### Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

## 📚 Documentación de la API

La documentación interactiva está disponible cuando el servidor está en ejecución:

- **Swagger UI (Interactivo):** `http://localhost:8000/api/v1/docs`
- **ReDoc (Documentación alternativa):** `http://localhost:8000/api/v1/redoc`

### Endpoints Disponibles

#### Marcas (`/api/v1/marcas/`)

- `GET /` - Lista todas las marcas
- `POST /` - Crea una nueva marca
- `GET /{id}` - Obtiene una marca por ID
- `PUT /{id}` - Actualiza una marca existente
- `DELETE /{id}` - Elimina una marca

## 🗃️ Base de Datos

La aplicación utiliza SQLite por defecto, con la base de datos `marcas.db` que se crea automáticamente en el directorio raíz durante el primer inicio.

### Migraciones

Para crear una nueva migración con Alembic:

```bash
alembic revision --autogenerate -m "descripcion del cambio"
alembic upgrade head
```

## 🚀 Despliegue

### Railway

1. Instala la CLI de Railway:

   ```bash
   npm i -g @railway/cli
   ```

2. Inicia sesión:

   ```bash
   railway login
   ```

3. Despliega la aplicación:
   ```bash
   railway up
   ```

## 📄 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

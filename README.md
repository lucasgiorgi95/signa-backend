# Backend para Registro de Marcas

Una API simple hecha con FastAPI para manejar marcas comerciales. Usa SQLite así que no necesitas configurar nada complicado.

## Cómo empezar

Necesitas Python 3.8+ y ya.

1. Clona esto:
   ```bash
   git clone [tu-repo]
   cd signa-backend
   ```

2. Instala las cosas:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta:
   ```bash
   python run.py
   ```

Ya tienes el servidor corriendo en `http://localhost:8000`

## Variables de entorno

Si quieres cambiar algo, crea un `.env`:

```
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

## Qué hace

- Crear, ver, editar y borrar marcas
- Base de datos SQLite (se crea sola)
- Documentación automática en `/api/v1/docs`



Los archivos importantes:
- `main.py` - Donde se configura FastAPI y CORS
- `database.py` - Conexión a SQLite
- `models/marca.py` - Modelo de Marca
- `api/v1/endpoints/marcas.py` - Todos los endpoints

## API

Una vez que esté corriendo, puedes ver la documentación en:
- `http://localhost:8000/api/v1/docs` - Swagger UI
- `http://localhost:8000/api/v1/redoc` - ReDoc

### Endpoints

**Marcas** (`/api/v1/marcas/`):
- `GET /` - Ver todas las marcas
- `POST /` - Crear marca nueva
- `GET /{id}` - Ver una marca
- `PUT /{id}` - Actualizar marca
- `DELETE /{id}` - Borrar marca

## Despliegue

Para subir a Render o Railway solo necesitas conectar el repo. Ya está configurado con los archivos necesarios.

La base de datos SQLite se crea automáticamente la primera vez que corres la app.

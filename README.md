# Mi Portafolio API

Backend de mi portafolio personal para el envío de emails desde el formulario de contacto.

## Instalación

1. Clonar el repositorio
2. Crear entorno virtual: `python3 -m venv venv`
3. Activar: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Crear `.env` con `EMAIL` y `PASSWORD`

## Correr el servidor
```bash
uvicorn main:app --reload
```

## Endpoints

- `GET /` → Health check
- `POST /contacto` → Envía email con los datos del formulario
# AgroSprint

## Iniciar en desarrollo

Desde la raíz del proyecto, crear y activar un entorno virtual, instalar Django y preparar la base de datos:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

La aplicación queda disponible en <http://127.0.0.1:8000/>.

En Debian/Ubuntu, si falla la creación del entorno porque falta `venv`, instalar el paquete correspondiente a la versión de Python (por ejemplo, `python3.12-venv`) y volver a ejecutar el primer comando.

Cuando descargues cambios que agregan o modifican campos y opciones, ejecuta `python manage.py migrate` para actualizar la base de datos.

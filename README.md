# Taller U3: Automatización de BD con Python, Faker y Git

Script en Python que crea una tabla en una base de datos MySQL local y la
puebla con 100.000 registros de datos falsos generados con Faker.

## Qué hace
1. Se conecta a MySQL con SQLAlchemy (credenciales en `.env`).
2. Crea la tabla `personas_juan` si no existe.
3. Genera 100.000 personas con Faker (locale `es_CO`).
4. Las inserta por lotes de 10.000 y verifica el total con un `COUNT(*)`.

## Tabla `personas_juan`
`id` (PK), `nombre`, `apellido`, `correo`, `fecha_nacimiento`, `ciudad`,
`direccion`, `telefono`, `empresa`, `profesion`.

## Requisitos
Python 3.10+, MySQL Server local y Git.

## Instalación
```bash
git clone https://github.com/Juandiegogomezz/taller-u3-faker-mysql-juangomez.git
cd taller-u3-faker-mysql-juangomez
python -m venv .venv
source .venv/Scripts/activate   # Git Bash en Windows
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración
Copia la plantilla y completa tus datos:
```bash
cp .env.example .env
```
Edita `.env` con tu usuario, contraseña, host, puerto y nombre de la base.
La base de datos debe existir previamente (`CREATE DATABASE taller_u3;`).

## Ejecución
```bash
python main.py
```
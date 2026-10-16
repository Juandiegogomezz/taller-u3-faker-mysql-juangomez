"""Taller U3: automatización de BD con Python, Faker y Git."""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

NOMBRE = "juan"
TABLA = f"personas_{NOMBRE}"


def crear_motor():
    """Crea el motor de SQLAlchemy leyendo las credenciales del archivo .env."""
    load_dotenv()
    url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME"),
    )
    return create_engine(url)


def main():
    engine = crear_motor()
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("Conexión exitosa a MySQL")


if __name__ == "__main__":
    main()
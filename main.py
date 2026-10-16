"""Taller U3: automatización de BD con Python, Faker y Git."""
import os

from dotenv import load_dotenv
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, create_engine, text
from sqlalchemy.engine import URL
from faker import Faker
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

def definir_tabla(metadata):
    """Define la estructura de la tabla: 1 PK + 9 atributos."""
    return Table(
        TABLA,
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100), nullable=False),
        Column("apellido", String(100), nullable=False),
        Column("correo", String(150), nullable=False),
        Column("fecha_nacimiento", Date, nullable=False),
        Column("ciudad", String(100)),
        Column("direccion", String(255)),
        Column("telefono", String(50)),
        Column("empresa", String(150)),
        Column("profesion", String(150)),
    )

def main():
    engine = crear_motor()
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("Conexión exitosa a MySQL")

    metadata = MetaData()
    tabla = definir_tabla(metadata)
    metadata.create_all(engine)
    print(f"Tabla '{TABLA}' lista")

def generar_personas(cantidad):
    """Genera una lista de diccionarios con datos falsos coherentes."""
    fake = Faker("es_CO")
    return [
        {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "correo": fake.email(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "ciudad": fake.city(),
            "direccion": fake.address().replace("\n", ", "),
            "telefono": fake.phone_number(),
            "empresa": fake.company(),
            "profesion": fake.job(),
        }
        for _ in range(cantidad)
    ]

if __name__ == "__main__":
    main()
muestra = generar_personas(3)    
for persona in muestra:
    print(persona)    
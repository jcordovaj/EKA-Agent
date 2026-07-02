import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from sqlalchemy import create_engine
from src.persistence.models import Base

# --- CAMBIO AQUÍ: Pasamos los parámetros por separado ---
# Esto evita que una URL sea parseada incorrectamente
engine = create_engine(
    "postgresql+psycopg2://",
    creator=lambda: __import__('psycopg2').connect(
        user="admin",
        password="password",
        host="localhost",
        port="5432",
        dbname="eka_db"
    )
)

def create_tables():
    try:
        Base.metadata.create_all(engine)
        print("¡Éxito! Tablas creadas en la base de datos.")
    except Exception as e:
        print(f"Error detallado: {e}")

if __name__ == "__main__":
    create_tables()
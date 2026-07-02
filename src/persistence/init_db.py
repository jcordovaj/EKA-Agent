import sys
import os

# Esto le dice a Python: "Añade la carpeta raíz del proyecto al camino de búsqueda"
# El archivo está en src/persistence/, así que subimos dos niveles para llegar a la raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from sqlalchemy import create_engine
from src.persistence.models import Base

DATABASE_URL = "postgresql+psycopg2://admin:password@localhost:5432/eka_db"

def create_tables():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("¡Éxito! Tablas creadas en la base de datos.")

if __name__ == "__main__":
    create_tables()
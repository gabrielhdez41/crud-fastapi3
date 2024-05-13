from pymongo import MongoClient # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de MongoDB del archivo .env
mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")

# Crear la conexión a MongoDB
conn_string = f"mongodb+srv://{mongo_username}:{mongo_password}@cluster0.j8vbz9m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
conn = MongoClient(conn_string)

# Continuar con tu lógica de aplicación utilizando la conexión a MongoDB
db = conn.todo_db
collection_name = db["todo_collection"]

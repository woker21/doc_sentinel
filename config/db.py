from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://syswoker:GECcsxusvA8IXTNs@docsentinel.qljo3sd.mongodb.net/?retryWrites=true&w=majority"

# Creamos una nueva conecion
conn = MongoClient(uri)

#seleccionamos la BD

db = conn['docsentinel']

#accedemos a la coleccion

coleccion = db['DocSentinel']

# Probamos la conexion
try:
    conn.admin.command('ping')
    print("Conectado a MongoDB Atlas :D")
except Exception as e:
    print("No se pudo conectar a MongoDB Atlas:", str(e))
import pymongo
import certifi

ca = certifi.where()


client = pymongo.MongoClient("mongodb+srv://MisionTic31:Mongo2022@cluster0.vb7qywf.mongodb.net/db-registro-academico?retryWrites=true&w=majority",tlsCAFile=ca)
baseDatos = client["db-registro-academico"]
print(baseDatos.list_collection_names())

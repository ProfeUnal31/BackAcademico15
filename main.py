from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from Routes.Estudiante import estudiante
from Routes.Departamento import departamento
from Routes.Inscripcion import inscripcion
from Routes.Materia import materia

app=Flask(__name__)
cors = CORS(app)

app.register_blueprint(estudiante)
app.register_blueprint(departamento)
app.register_blueprint(inscripcion)
app.register_blueprint(materia)

app.debug = True

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

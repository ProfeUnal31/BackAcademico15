from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        self.repositorioEstudiante = RepositorioEstudiante()

    def index(self):
        return self.repositorioEstudiante.findAll()

    def create(self, infoEstudiante):
        try:

            if infoEstudiante["cedula"] == None:
                pass
            if infoEstudiante["apellido"] == None:
                pass
            if infoEstudiante["nombre"] == None:
                pass
        except:
            return {"Mensaje": "No ingreso informacion valida para crear el Estudiante"}
    def show(self,id):
        elEstudiante=Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__
    def update(self,id,infoEstudiante):
        estudianteActual=Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula=infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]

        return self.repositorioEstudiante.save(estudianteActual)
    def delete(self,id):
        return self.repositorioEstudiante.delete(id)


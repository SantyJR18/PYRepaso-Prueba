class Estudiante:
    def __init__(self, id, nom, ape, car, notas):
        self.Id = id
        self.Nombres = nom
        self.Apellidos = ape
        self.Carrera = car
        self.Notas = notas

class Nota:
    def __init__(self, mat, cal):
        self.Materia = mat
        self.Calificacion = cal
        
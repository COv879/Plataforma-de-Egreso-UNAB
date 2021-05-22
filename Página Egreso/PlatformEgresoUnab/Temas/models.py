from django.db import models

estado = [('Activo', 'Activo'), ('Asignado', 'Asignado')]
professores = [('Professor 1', 'Professor 1'), ('Professor 2', 'Professor 2')]

class Tema(models.Model):
    nombre_professor = models.CharField(max_length=50, choices=professores)
    #palabras_clave = models.CharField(max_length=70)
    nombre_tema = models.CharField(max_length=60)
    #descripcion = models.CharField(max_length=800)
    estado = models.CharField(max_length=15)

class TemaEjemplo:
    def __init__(self):
        self.temas = []
        self.temas.append(Tema("Profesor 1", "Tema 1", "Activo"))
        self.temas.append(Tema("Profesor 2", "Tema 2", "Activo"))
        self.temas.append(Tema("Profesor 3", "Tema 3", "Asignado"))

    def obtenerTemas(self):
        return self.temas


# Create your models here.

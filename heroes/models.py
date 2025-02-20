from django.db import models



class Heroes(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    edad = models.IntegerField()
    poder = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    descripcion = models.TextField()


    '''def __str__(self):
        return self.nombre'''
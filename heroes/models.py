from django.db import models



class Heroes(models.Model):
    nombre = models.CharField(max_length=100)
    img = models.ImageField(upload_to='heroes', blank=True, null=True)
    alias = models.CharField(max_length=100)
    edad = models.IntegerField()
    poder = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    descripcion = models.TextField()
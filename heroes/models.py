from django.db import models
import uuid



class Heroes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    edad = models.IntegerField()
    poder = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    descripcion = models.TextField()
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)



    USERNAME_FIELD = 'email' # Mediante esta config pediremos como parametro de entrada el email y password en el panel de administración
    REQUIRED_FIELDS = []

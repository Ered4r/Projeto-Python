from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoa(AbstractUser):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)       
    def __str__(self):
        return self.nome
  
 
# Create your models here.

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.CharField(max_length=150, null=False, blank=False)
    password = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.username
        
    @classmethod
    def get_by_id(cls):
        pass
        
        
class workerModel(models.Model):   

    id = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=20, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=200, null=False, blank=False)
    adscripcion = models.CharField(max_length=200, null=False, blank=False)
    turno = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    createdat = models.DateTimeField(default=datetime.now())
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula
    
    
class childModel(models.Model):

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    f_nac = models.CharField(max_length=200, null=False, blank=False)
    edad = models.FloatField()
    sexo = models.CharField(max_length=20, null=False, blank=False)
    entregado = models.CharField(max_length=100, null=True, blank=True)
    createdat = models.DateTimeField(default=datetime.now())
    worker_id = models.ForeignKey(workerModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre    

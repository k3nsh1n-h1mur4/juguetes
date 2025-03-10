from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'users'

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
    class Meta:
        db_table = 'worker'

    id = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=20, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=200, null=False, blank=False)
    antiguedad = models.CharField(max_length=30, null=True, blank=False)
    adscripcion = models.CharField(max_length=200, null=False, blank=False)
    t_contr = models.CharField(max_length=30, null=True, blank=False)
    turno = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    domicilio = models.CharField(max_length=250, null=True, blank=False)
    telefono = models.CharField(max_length=30, null=True, blank=False)
    sexo = models.CharField(max_length=20, null=True, blank=False)
    edad = models.CharField(max_length=2, null=True, blank=False)
    createdat = models.DateTimeField()
    user_id = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.matricula
    
    
class childModel(models.Model):
    class Meta:
        db_table = 'chailds'

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    f_nac = models.CharField(max_length=200, null=True, blank=True)
    edad = models.FloatField()
    sexo = models.CharField(max_length=20, null=False, blank=False)
    entregado = models.CharField(max_length=100, null=True, blank=True)
    #qrimg = models.BinaryField()
    createdat = models.DateTimeField()
    worker_id = models.ForeignKey(workerModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre    

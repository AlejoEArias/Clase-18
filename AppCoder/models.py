from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class familiar (models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
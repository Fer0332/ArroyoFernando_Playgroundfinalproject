from django.db import models

# Create your models here.
class termo(models.Model): 
    marca = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    color = models.CharField(max_length=20)
    linea = models.CharField(max_length=20)
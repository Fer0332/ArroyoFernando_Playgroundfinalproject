from django.db import models
from ckeditor.fields import RichTextField

class Mate(models.Model): 
    marca = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.marca}{self.capacidad}{self.color}{self.tipo}"


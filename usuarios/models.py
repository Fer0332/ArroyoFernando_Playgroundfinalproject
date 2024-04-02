from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class DatosExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    
    def __str__(self):
        return f'Datos adicionales del Usuario {self.user}'

# Función para crear automáticamente DatosExtras cada vez que se crea un nuevo usuario
@receiver(post_save, sender=User)
def create_datos_extras(sender, instance, created, **kwargs):
    if created:
        DatosExtras.objects.create(user=instance)





# from django.db import models
# from django.contrib.auth.models import User

# class DatosExtras(models.Model):
#     user = models.OneToOneField(User, on_delete= models.CASCADE)
#     avatar = models.ImageField(upload_to= "avatares", null=True, blank=True)
    
#     def __str__(self):
#         return f'Datos adicionales del Usuario {self.user}'

# # Create your models here.

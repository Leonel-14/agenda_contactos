from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    numero = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.nombre}{self.email}{self.numero}"
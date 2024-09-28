from django.db import models

# Create your models here.
class nfc(models.Model):  # Es recomendable usar PascalCase para los nombres de las clases
    dinero = models.IntegerField()
    idUser = models.IntegerField()
    nombre = models.CharField(max_length=30)  # Corrige 'max_lenght' a 'max_length'
    
    def __str__(self):
        return str(self.pk)  # Convierte 'self.pk' a cadena para evitar errores
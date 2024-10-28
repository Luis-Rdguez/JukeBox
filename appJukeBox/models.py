from django.db import models

# Create your models here.

class Banda(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField()
    fechaIni = models.DateField()
    fechaFin = models.DateTimeField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    estilos = models.ManyToManyField(Estilo)
    
    def __str__(self):
        return self.nombre
    
class Pais(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    cod_pais = models.CharField(max_length=2)
    pais = models.CharField(max_length=30)
    def __str__(self):
        return self.pais
    

class Estilo(models.Model):

    cod_estilo = models.CharField(3)
    estilo = models.CharField()

    def __str__(self):
        return self.nombre	

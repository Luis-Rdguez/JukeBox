from django.db import models

class Pais(models.Model):
    cod_pais = models.CharField(max_length=2)
    pais = models.CharField(max_length=30)
    bandera = models.URLField(max_length=700)

    def numero_bandas(self):
        return self.banda_set.count()

    def __str__(self):
        return f"{self.pais} (Bandas: {self.numero_bandas()})"

class Estilo(models.Model):
    cod_estilo = models.CharField(max_length=3)
    estilo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def numero_bandas(self):
        return self.banda_set.count()

    def __str__(self):
        return f"{self.estilo} (Bandas: {self.numero_bandas()})"

class Banda(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fechaIni = models.DateField()
    fechaFin = models.DateField(null=True, blank=True)
    foto = models.URLField(max_length=700)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    estilos = models.ManyToManyField(Estilo)
    
    def __str__(self):
        return self.nombre

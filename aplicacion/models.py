from django.db import models

# Create your models here.

from django.db import models

class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad= models.DecimalField(max_digits=10, decimal_places=2)

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.FloatField()

class Verdura (models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    unidad= models.DecimalField(max_digits=10, decimal_places=2)

class Fruta(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    unidad= models.DecimalField(max_digits=10, decimal_places=2)
from urllib import request
from django.conf import settings
from django.db import models
from django.utils import timezone


class Comuna(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

class Tipodemanda(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre



class Demanda(models.Model):
    id_demanda = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    detalle = models.TextField()
    tipodemanda = models.ForeignKey(Tipodemanda, on_delete=models.CASCADE,blank=True,null=True)
    rut1 = models.IntegerField(null=True,blank=True)
    dv1 = models.CharField(max_length=2,null=True,blank=True,default='')
    nombre1 = models.CharField(max_length=25,null=True,blank=True,default='')
    apellido1 = models.CharField(max_length=25,null=True,blank=True,default='')
    telefono1 = models.IntegerField(null=True,blank=True)
    comuna1 = models.ForeignKey(Comuna,related_name='comuna1',on_delete=models.CASCADE,null=True,blank=True)
    rut2 = models.IntegerField(null=True,blank=True)
    dv2 = models.CharField(max_length=2,null=True,blank=True,default='')
    nombre2 = models.CharField(max_length=30,null=True,blank=True,default='')
    apellido2 = models.CharField(max_length=25,null=True,blank=True,default='')
    telefono2 = models.IntegerField(null=True,blank=True)
    comuna2 = models.ForeignKey(Comuna,related_name='comuna2',on_delete=models.CASCADE,null=True,blank=True)


    def __Str__(self):
        return self.id_demanda
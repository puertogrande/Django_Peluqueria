from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Peluquero(models.Model):
    DNI = models.CharField(primary_key=True,max_length=9,default='11111587d')
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    trabajaMujer = models.BooleanField(default=True)
    trabajaHombre = models.BooleanField(default=True)
    imagen= models.ImageField(null=True, upload_to="fotos/")
    descripcion=models.CharField(max_length=500,null=True)
    
    def __str__(self):
        return self.nombre +" "+self.apellidos 

class Servicio(models.Model):
    GENERO_CHOICES = (("Hombre", "Hombre"),("Mujer", "Mujer"),) 
    genero = models.CharField(max_length=7,choices=GENERO_CHOICES,default=2)
    nombre = models.CharField(primary_key=True,max_length=20,default='pelado')    
    precio = models.IntegerField(default=10)

    def __str__(self):
        return self.genero+" "+self.nombre +" "+str(self.precio) +" euros"
    
class Cliente(models.Model):
    GENERO_CHOICES = (("Hombre", "Hombre"),("Mujer", "Mujer"),)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    nombre= models.CharField(max_length=20,primary_key=True,default='rafa')
    apellidos= models.CharField(max_length=60)
    imagen= models.ImageField(null=True, upload_to="fotos/")
    genero= models.CharField(max_length=7,choices=GENERO_CHOICES,default="Mujer")
    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
    peluquero=models.ForeignKey(Peluquero,on_delete=models.CASCADE,null=True)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE,null=True)
    hora=models.DateTimeField(null=True, blank=True)
    hora_js=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.cliente.nombre +" te va a hacer un "+self.servicio.nombre+" "+self.peluquero.nombre+" "+str(self.hora)

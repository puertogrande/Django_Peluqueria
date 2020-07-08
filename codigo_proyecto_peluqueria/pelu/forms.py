from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Peluquero,Servicio,Cliente
from django.contrib.auth.models import User


class ClienteForm(ModelForm):
    nombre = forms.CharField(max_length=30)
    correo= forms.CharField(max_length=30)
    contrasena= forms.CharField(max_length=30,widget=forms.PasswordInput)
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos','genero','imagen']


class PeluqueroForm(ModelForm):
    class Meta:
        model = Peluquero
        fields = ['DNI','nombre', 'apellidos', 'trabajaMujer', 'trabajaHombre','imagen','descripcion']

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['genero','nombre','precio']


class InicioForm(forms.Form): 
    #nombre = forms.CharField(max_length=30)
    correo= forms.CharField(max_length=30)
    contrasena= forms.CharField(max_length=30,widget=forms.PasswordInput)

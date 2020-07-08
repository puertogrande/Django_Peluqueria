from django.contrib import admin
from .models import Cliente,Peluquero,Servicio,Trabajo


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Peluquero)
admin.site.register(Servicio)
admin.site.register(Trabajo)
print("al menos me ha llevado aqui")
from django.urls import path
from . import views
urlpatterns = [
    
    
    path('registrar/', views.registro, name='registros'),
    path('principal/', views.principal, name='peluquero'),
    path('logout/', views.logout, name='peluquero'),
    path('', views.principal, name='peluquero'),
    path('peluquero/', views.peluquero, name='peluquero'),
    path('servicio/', views.servicio, name='peluquero_alta'),
    path('servicios_usuario/', views.serviciosUsuario, name='servicios'),
    path('peluqueros_usuario/', views.peluquerosUsuario, name='peluquero'),
    path('cita/', views.cita, name='peluquero'),
    path('cita_ajax/', views.cita_ajax, name='peluquero'),
    path('procesamiento_ajax/', views.procesamiento_ajax, name='peluquero'),
    path('procesar/',views.procesar, name='peluquero'),
]
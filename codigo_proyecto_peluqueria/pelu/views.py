from django.shortcuts import render, redirect, get_object_or_404
from .models import Peluquero,Cliente,Servicio,Trabajo
from .forms import ClienteForm,ServicioForm,PeluqueroForm,InicioForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from datetime import datetime  
from datetime import timedelta  
import time
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request,"principal.html", {})
    

@login_required
def principal(request):
    print("/////")
    
    print(request.user.username)
    
    return render(request,"principal.html", {})


def registro(request):
    if request.POST:
        form = ClienteForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            # Crea un nuevo usuario en django
            nuevo_usuario = User.objects.create_user(form['nombre'].value(),form['correo'].value(),form['contrasena'].value())
            nuevo_usuario.save()
            # Crea un Alumno desde los campos del formulario
            nuevo_cliente= form.save()
            # Asocia el usuario django creado antes con el nuevo alumno
            nuevo_cliente.usuario = nuevo_usuario
            nuevo_cliente.save()

            #redireccionar donde se muestran los servicios para la peluqueria
            return HttpResponseRedirect('/principal/')
    else:
        form = ClienteForm()
    return render(request,"alta_cliente.html", {'form': form})

# Create your views here.
#solo si el usuario es administrador
@user_passes_test(lambda u: u.is_superuser)
def peluquero(request):  
    if request.POST:
        form = PeluqueroForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/principal/')
    else:
        form = PeluqueroForm()
    return render(request,"alta_cliente.html", {'form': form})


# Create your views here.
#solo si el usuario es administrador
@user_passes_test(lambda u: u.is_superuser)
def servicio(request):  
    if request.POST:
        form = ServicioForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
    else:
        form = ServicioForm()
    return render(request,"alta_cliente.html", {'form': form})

@login_required
def serviciosUsuario(request):
    print("este es el usuario")
    print(request.user.username)
    usuario=request.user.username
    cliente=Cliente.objects.get(usuario=request.user)
    genero=cliente.genero
    nombre=cliente.nombre
    if genero=="Hombre":
        servicios=Servicio.objects.filter(genero="Hombre")
        for servicio in servicios:
            print (servicio)
    else:
        servicios_disponible=Servicio.objects.filter(genero="Mujer")
    return render(request,"servicio_usuario.html", {'servicios': servicios})
    
@login_required
def peluquerosUsuario(request):
    print("este es el usuario")
    print(request.user.username)
    usuario=request.user.username
    
    cliente=Cliente.objects.get(usuario=request.user)
    genero=cliente.genero
    if genero=="Hombre":
        peluqueros=Peluquero.objects.filter(trabajaHombre=True)
    else:
        peluqueros=Peluquero.objects.filter(trabajaMujer=True)
    return render(request,"peluqueros_usuario.html", {'peluqueros': peluqueros})
@login_required
def cita(request):
    usuario=request.user.username
    cliente=Cliente.objects.get(usuario=request.user)
    genero=cliente.genero
    trabajos=Trabajo.objects.all()
    for trabajo in trabajos:
        print(trabajo)

    if genero=="Hombre":
        servicios=Servicio.objects.filter(genero="Hombre")
        peluqueros=Peluquero.objects.filter(trabajaHombre=True)
    else:
        servicios=Servicio.objects.filter(genero="Mujer")
        peluqueros=Peluquero.objects.filter(trabajaMujer=True)

    dia=datetime.now()
    print(dia)
    horasTrabajo=[["Elige la cita","Elige la cita"]]
    manana=dia+ timedelta(days=1) 
    manana=manana.replace(hour=10, minute=00,second=00,microsecond=00)
    cierre=manana.replace(hour=17,minute=00,second=00,microsecond=00)
    while manana < cierre:
        manana=manana+timedelta(minutes=30)
        string_manana= manana.strftime("%m/%d/%y %H:%M")
        horita=[int(time.mktime(manana.timetuple())) * 1000,manana]
        horasTrabajo.append(horita)
         
    return render(request,"cita.html",{'peluqueros': peluqueros,'servicios': servicios,'horasTrabajo': horasTrabajo,'trabajos': trabajos,
    })
    
@login_required
@csrf_exempt
def cita_ajax(request):
    usuario=request.user.username
    cliente=Cliente.objects.get(usuario=request.user)
    genero=cliente.genero
    trabajos=Trabajo.objects.all()
    if genero=="Hombre":
        servicios=Servicio.objects.filter(genero="Hombre")
        peluqueros=Peluquero.objects.filter(trabajaHombre=True)
    else:
        servicios=Servicio.objects.filter(genero="Mujer")
        peluqueros=Peluquero.objects.filter(trabajaMujer=True)

    dia=datetime.now()
    horasTrabajo=[["Elige la cita","Elige la cita"]]
    manana=dia+ timedelta(days=1) 
    manana=manana.replace(hour=10, minute=00,second=00,microsecond=00)
    cierre=manana.replace(hour=17,minute=00,second=00,microsecond=00)
    while manana < cierre:
        manana=manana+timedelta(minutes=30)
        string_manana= manana.strftime("%m/%d/%y %H:%M")
        horita=[int(time.mktime(manana.timetuple())) * 1000,manana]
        horasTrabajo.append(horita)
         
    return render(request,"cita_ajax.html",{'peluqueros': peluqueros,'servicios': servicios,'horasTrabajo': horasTrabajo,'trabajos': trabajos,
    })
@login_required
@csrf_exempt
def procesamiento_ajax(request):
    if request.POST:
        dni_peluquero = request.POST.get('DNI',None)
        peluquero_seleccionado=Peluquero.objects.get(DNI=dni_peluquero)
        trabajos_peluquero=Trabajo.objects.filter(peluquero=peluquero_seleccionado)
        horas_cogidas=[]

        for trabajo in trabajos_peluquero:
            hora=trabajo.hora
            horas_cogidas.append(trabajo.hora_js)
       
        dia=datetime.now()
        manana=dia+ timedelta(days=1) 
        manana=manana.replace(hour=10, minute=00,second=00,microsecond=00)
        cierre=manana.replace(hour=17,minute=00,second=00,microsecond=00)
        horasTrabajo=[]
        while manana < cierre:
            manana=manana+timedelta(minutes=30)
            string_manana= manana.strftime("%m/%d/%y %H:%M")
            horita_comprobar=int(time.mktime(manana.timetuple())) * 1000
            horita_comprobar=str(horita_comprobar)
            
            if horita_comprobar in horas_cogidas:
                print("esa hora ya esta cogida!!!!!!!")
                continue
            else:
                horasTrabajo.append([horita_comprobar,manana]) 
        print(repr(horasTrabajo))
        diccionario = { "libres" : horasTrabajo }
        return JsonResponse(diccionario)
    else:
        return JsonResponse({ "libres" : [] })

    
    #response = JsonResponse([1, 2, 3], safe=False)
    #peluqueros=Peluquero.objects.filter(trabajaHombre=True)

    #return render(request,"peluqueros_usuario.html", {'peluqueros': peluqueros})

def procesar(request):
    print("print el formulario ha sido procesado")
    if request.POST:
        peluquero=request.POST.get('peluquero')
        servicio=request.POST.get('servicio')
        hora=request.POST.get('hora')
        print(hora)
        print(type(hora))
        segundos=int(hora)/1000
        fecha=datetime.fromtimestamp(segundos)
        print(fecha)
        cliente=Cliente.objects.get(usuario=request.user)
        peluquero=Peluquero.objects.get(DNI=peluquero)
        servicio=Servicio.objects.get(nombre=servicio)        
        trabajo_guardado = Trabajo(cliente=cliente, peluquero=peluquero,servicio=servicio,hora=fecha,hora_js=hora)
        trabajo_guardado.save()
        #seleccionar todas las fechas de los objetos y comprobar si coincide con la fecha date
        print(trabajo_guardado)
       
def procesar_cita(request):
    if request.POST:
        print("se ha enviado una peticion")

        """id_seleccionado=//conseguir el id
        a partir de trabajos
        trabajos_peluquero=Trabajo.objects.filter(cliente_id=id_seleccionado)
        horas_cogidas=[]

        for peluquero in trabajos_peluquero:
            hora=peluquero.hora
            horas_cogidas.append(hora_js)

        dia=datetime.now()
        manana=dia+ timedelta(days=1) 
        manana=manana.replace(hour=10, minute=00,second=00,microsecond=00)
        cierre=manana.replace(hour=17,minute=00,second=00,microsecond=00)
        horasTrabajo=[]
        while manana < cierre:
            manana=manana+timedelta(minutes=30)
            string_manana= manana.strftime("%m/%d/%y %H:%M")
            horita_comprobar=int(time.mktime(manana.timetuple())) * 1000

            if horita_comprobar in horas_cogidas:
                continue
            else:
                horita=[horita_comprobar,manana]
                horasTrabajo.append(horita)"""

                  



        




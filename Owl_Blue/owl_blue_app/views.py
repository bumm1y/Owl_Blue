from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Categoria, Explicaciones, Actividades
from django.contrib.auth.decorators import login_required
from random import sample

''' Respuestas JSON '''
def lessonJSON(request, categoria_elegida):
    actividades = request.session.get('actividades', [])
    response = {'actividades': actividades}
    return JsonResponse(response)


''' Cápsula 0 '''
@login_required
def capsula0(request, categoria_elegida):
    explicaciones = list(Explicaciones.objects.filter(categoria__categoria=categoria_elegida))
    return render(request, 'owl_blue_app/capsula0.html', {'categoria_elegida': categoria_elegida, 'explicaciones': explicaciones})


''' Prueba lessons.html '''
@login_required
def lessons(request, categoria_elegida):
    seleccion = sample(range(1,11), 5)
    categoria = categoria_elegida
    actividades = list(Actividades.objects.filter(categoria__categoria=categoria, num_pregunta__in=seleccion))
    request.session['actividades'] = [{'categoria' : categoria, 'num_pregunta': actividad.num_pregunta, 'pregunta': actividad.pregunta, 'videos': actividad.videos, 'respuesta': actividad.respuesta, 'alternativa1': actividad.alternativa1, 'alternativa2': actividad.alternativa2, 'alternativa3': actividad.alternativa3} for actividad in actividades]
    return render(request, 'owl_blue_app/lessons.html', {'categoria': categoria, 'actividades': actividades})

# Página home
def index(request):
    mensaje_confirmacion = request.session.pop('mensaje_confirmacion', None) # <-- Verifica el mensaje de confirmación
    return render(request, 'owl_blue_app/index.html', {'mensaje_confirmacion': mensaje_confirmacion})# <-- 'Carga' la página home y envía el mensaje de confirmación

# Registro de usuarios
def signup(request):
    ''' Traspasa los datos entregados en html al SignupForm'''
    if request.method == 'GET':
        form = SignupForm() # <-- formulario personalizado
        return render(request, 'owl_blue_app/signup.html', {'form' : form}) # <-- 'Carga' la página signup
    else:
        form = SignupForm()
        try:
            user = User.objects.create_user(email=request.POST['email'],
            username=request.POST['username'], password=request.POST['password1'])
            user.save() # <-- Guardado en BBDD
            login(request, user)
            mensaje_confirmacion = f"¡Usuario creado exitosamente!"
            request.session['mensaje_confirmacion'] = mensaje_confirmacion
            return redirect('home')
        except IntegrityError:
            return render(request, 'owl_blue_app/signup.html', {
        'form': form, 'error': 'El usuario o correo ingresado ya existe.'})

# Login
def signin(request):
    form = LoginForm()
    ''' Si se visita sin autenticarse... '''
    if request.method == 'GET':
        return render(request, 'owl_blue_app/signin.html', {
            'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST[
            'password'
        ])
        if user is None:
            return render(request, 'owl_blue_app/signin.html', {
                'form': form, 'error': 'El usuario o la contraseña son incorrectos.'})
        else:
            mensaje_confirmacion = f"Bienvenido de vuelta!"
            request.session['mensaje_confirmacion'] = mensaje_confirmacion
            login(request, user)
            return redirect('home')
# Logout
def signout(request):
    logout(request)
    return redirect('home') 

''' Actividades() '''

@login_required # Se necesita estar logeado para ingresar a actividades
def acts(request):
    acts = Categoria.objects.all()
    return render(request, 'owl_blue_app/acts.html', {
        'acts': acts})

@login_required
def abc(request):
    categoria_elegida="Abecedario"
    return render(request, 'owl_blue_app/abc.html', {'categoria_elegida': categoria_elegida})

@login_required
def preguntas(request):
    categoria_elegida="Preguntas"
    return render(request, 'owl_blue_app/preguntas.html', {'categoria_elegida': categoria_elegida})

@login_required
def emociones(request):
    categoria_elegida="Emociones"
    return render(request, 'owl_blue_app/preguntas.html', {'categoria_elegida': categoria_elegida})

@login_required
def familia(request):
    categoria_elegida="Familia"
    return render(request, 'owl_blue_app/preguntas.html', {'categoria_elegida': categoria_elegida})

""" Vista cuenta """
@login_required
def myaccount(request):
    return render(request, 'owl_blue_app/myaccount.html')
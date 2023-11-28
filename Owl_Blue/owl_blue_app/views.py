from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, EdicionPerfilForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Categoria, Explicaciones, Actividades, InfoUsuario, ProgresoLecciones
from django.contrib.auth.decorators import login_required
from random import sample


''' Respuestas JSON '''
@login_required
def lessonJSON(request, categoria_elegida):
    actividades = request.session.get('actividades', [])
    response = {'actividades': actividades} # datos en formato JSON
    return JsonResponse(response)

@login_required
def failedlesson(request, categoria_elegida):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    return render(request, 'owl_blue_app/failedlesson.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})


@login_required
def completelesson(request, categoria_elegida):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    user = request.user
    categoria = Categoria.objects.get(categoria=categoria_elegida)
    progreso, created = ProgresoLecciones.objects.get_or_create(user=user, topico=categoria)
    if not progreso.flag: # Verifica el estado de flag
        progreso.flag = True
        progreso.save() 
    return render(request, 'owl_blue_app/completelesson.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})

''' Cápsula 0 '''
@login_required
def capsula0(request, categoria_elegida):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    explicaciones = list(Explicaciones.objects.filter(categoria__categoria=categoria_elegida))
    return render(request, 'owl_blue_app/capsula0.html', {'categoria_elegida': categoria_elegida, 'explicaciones': explicaciones, "info_user": info_user})


''' Prueba lessons.html '''
@login_required
def lessons(request, categoria_elegida):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    seleccion = sample(range(1,11), 5) # selección indice
    categoria = categoria_elegida
    actividades = list(Actividades.objects.filter(categoria__categoria=categoria, num_pregunta__in=seleccion)) # extracción preguntas
    request.session['actividades'] = [{'categoria' : categoria, 'num_pregunta': actividad.num_pregunta, 'pregunta': actividad.pregunta, 'videos': actividad.videos, 'respuesta': actividad.respuesta, 'alternativa1': actividad.alternativa1, 'alternativa2': actividad.alternativa2, 'alternativa3': actividad.alternativa3} for actividad in actividades]
    return render(request, 'owl_blue_app/lessons.html', {'categoria': categoria, 'actividades': actividades, "info_user": info_user})

# Página home
def index(request):
    info_user = None
    if request.user.is_authenticated:
        info_user = InfoUsuario.objects.get(username=request.user.username)
    mensaje_confirmacion = request.session.pop('mensaje_confirmacion', None) # <-- Verifica el mensaje de confirmación
    return render(request, 'owl_blue_app/index.html', {'mensaje_confirmacion': mensaje_confirmacion, "info_user": info_user})# <-- 'Carga' la página home y envía el mensaje de confirmación

# Registro de usuarios
def signup(request):
    ''' Traspasa los datos entregados en html al SignupForm'''
    if request.method == 'GET':
        form = SignupForm() # <-- formulario personalizado
        return render(request, 'owl_blue_app/signup.html', {'form' : form}) # <-- 'Carga' la página signup
    else:
        ''' Tratamiento de datos enviados'''
        form = SignupForm(request.POST)
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        ''' Verificación de usuario en bbdd '''
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'owl_blue_app/signup.html', { 
                'form': form, 'error': 'El usuario o correo ingresado ya existe.'})
        else:
            ''' Creación del usuario en modelos pertinentes'''
            user = User.objects.create_user(email=email,
            username=username, password=password)
            user.save() # <-- Guardado en BBDD
            info_user = InfoUsuario(username=user.username)
            info_user.save()
            login(request, user)
            mensaje_confirmacion = f"¡Usuario creado exitosamente!"
            request.session['mensaje_confirmacion'] = mensaje_confirmacion
            return redirect('home')
       

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
    info_user = InfoUsuario.objects.get(username=request.user.username)
    acts = Categoria.objects.all()
    return render(request, 'owl_blue_app/acts.html', {
        'acts': acts, "info_user": info_user})

@login_required
def abc(request):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    categoria_elegida="Abecedario"
    return render(request, 'owl_blue_app/abc.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})

@login_required
def preguntas(request):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    categoria_elegida="Preguntas"
    return render(request, 'owl_blue_app/preguntas.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})

@login_required
def emociones(request):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    categoria_elegida="Emociones"
    return render(request, 'owl_blue_app/emociones.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})

@login_required
def familia(request):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    categoria_elegida="Familia"
    return render(request, 'owl_blue_app/familia.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})

@login_required
def casa(request):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    categoria_elegida="Casa"
    return render(request, 'owl_blue_app/casa.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})

@login_required
def escuela(request):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    categoria_elegida="Escuela"
    return render(request, 'owl_blue_app/escuela.html', {'categoria_elegida': categoria_elegida, "info_user": info_user})

""" Vista cuenta """
@login_required
def myaccount(request):
    user = request.user
    info_user = InfoUsuario.objects.get(username=request.user.username)
    progreso_lecciones = ProgresoLecciones.objects.filter(user=user) #progreso lecciones
    return render(request, 'owl_blue_app/myaccount.html', {"info_user": info_user, "progreso_lecciones": progreso_lecciones})

@login_required
def editar_perfil(request):
    info_user = InfoUsuario.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EdicionPerfilForm(request.POST, instance=info_user) #se visualiza el formulario
        if form.is_valid():
            form.save() #se guardan los cambios
            return redirect('myaccount')
    else:
        form = EdicionPerfilForm(instance=info_user) # se mantienen los cambios anteriores
    return render(request, 'owl_blue_app/editar_perfil.html', {'form': form, "info_user": info_user})
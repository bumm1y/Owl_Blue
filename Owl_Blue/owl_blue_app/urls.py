from django.urls import path, re_path
from .views import index, signup, signin, signout, acts, myaccount, abc, preguntas, emociones, familia, capsula0

''' Rutas para las distintas vistas '''
urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='lognin'),
    path('logout/', signout, name='logout'),
    path('acts/', acts, name='acts'),
    path('acts/abecedario', abc, name='abc'),
    path('acts/preguntas', preguntas, name='preguntas'),
    path('acts/emociones', emociones, name='emociones'),
    path('acts/familia', familia, name='familia'),
    path('myaccount/', myaccount, name='myaccount')
]
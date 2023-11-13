from django.urls import path
from .views import index, signup, signin, signout, acts, myaccount, abc, preguntas, emociones, familia, capsula0, lessons, lessonJSON, completelesson, failedlesson

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
    path('acts/<str:categoria_elegida>/capsula0/', capsula0, name='capsula0'),
    path('myaccount/', myaccount, name='myaccount'),
    path('acts/<str:categoria_elegida>/capsula0/lessons/', lessons, name='lessons'),
    path('acts/<str:categoria_elegida>/capsula0/lessons/lessonJSON', lessonJSON, name='lessonJSON'),
    path('<str:categoria_elegida>/completelesson/', completelesson, name='completelesson'),
    path('<str:categoria_elegida>/failedlesson/', failedlesson, name='failedlesson')    
]
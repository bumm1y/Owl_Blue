from django.urls import path
from .views import index, signup, signin, signout, acts

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='lognin'),
    path('logout/', signout, name='logout'),
    path('acts/', acts, name='acts')
]
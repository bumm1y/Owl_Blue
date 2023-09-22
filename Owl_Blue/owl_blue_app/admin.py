from django.contrib import admin
from .models import Categoria, Abecedario, Explicaciones, Actividades, Usuarios
''' 

** Credenciales user admin
--> user: admin
--> passwd: admin 

'''

admin.site.register(Categoria)
admin.site.register(Abecedario)
admin.site.register(Explicaciones)
admin.site.register(Usuarios)
admin.site.register(Actividades)


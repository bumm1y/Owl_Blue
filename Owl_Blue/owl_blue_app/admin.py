from django.contrib import admin
from .models import Categoria, Abecedario, Explicaciones, Actividades, Usuarios, InfoUsuario, ProgresoLecciones

admin.site.register(ProgresoLecciones)
admin.site.register(Categoria)
admin.site.register(Abecedario)
admin.site.register(Explicaciones)
admin.site.register(Usuarios)
admin.site.register(Actividades)
admin.site.register(InfoUsuario)


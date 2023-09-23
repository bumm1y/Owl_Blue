from django.db import models

''' Tablas de contenido '''

class Abecedario(models.Model):
    idabc = models.AutoField(primary_key=True)
    letra = models.CharField(max_length=1, unique=True)
    linkimg = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return f"{self.idabc}, {self.letra}, {self.linkimg}"
    
''' Foerign Key '''

class Categoria(models.Model):
    nom_categoria = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nom_categoria
    
''' Tabla de explicaciones'''

class Explicaciones(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img = models.CharField(max_length=1000, unique=True)
    vid = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return f"{self.categoria}, {self.img}, {self.vid}"

''' Tabla de actividades '''

class Actividades(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    videos = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.categoria}, {self.videos}"

''' Tabla de usuarios registrados '''

class Usuarios(models.Model):
    username = models.CharField(max_length=16, unique=True)
    email = models.CharField(max_length=50, unique=True)
    passwd = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.username}, {self.email}, {self.passwd}"


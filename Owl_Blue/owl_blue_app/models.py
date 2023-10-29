from django.db import models
from django.core import validators
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

''' Funciones de formularios '''
def validation_passwd(value):
    if not any(char.islower() for char in value): #Ciclo for para verificar si hay minúsculas
        raise ValidationError('La contraseña debe incluir una minúscula')
    if not any(char.isupper() for char in value): #Ciclo para verificar si hay mayúsculas
        raise ValidationError('La contraseña debe incluir una mayúscula')
    if not any(char.isdigit() for char in value): #Ciclo para ver si hay dígitos
        raise ValidationError('La contraseña debe incluir un dígito')
    
''' Tablas de contenido '''

class Abecedario(models.Model):
    idabc = models.AutoField(primary_key=True)
    letra = models.CharField(max_length=1, unique=True)
    linkimg = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return f"{self.idabc}, {self.letra}, {self.linkimg}"


''' Foreign Key '''

class Categoria(models.Model):
    categoria = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.categoria
    
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
    pregunta = models.CharField(max_length=100, default="")
    videos = models.CharField(max_length=1000, unique=True)
    respuesta = models.CharField(max_length=100, default="")
    alternativa1 = models.CharField(max_length=100, unique=True, default="")
    alternativa2 = models.CharField(max_length=100, unique=True, default="")
    alternativa3 = models.CharField(max_length=100, unique=True, default="")

    def __str__(self):
        return f"{self.categoria}, {self.pregunta}, {self.videos}, {self.respuesta}, {self.alternativa1}, {self.alternativa2}, {self.alternativa3}"

''' Tabla de usuarios registrados '''

class UsuariosForm(models.Model):
    username = models.CharField(max_length=16, unique=True, validators=[validators.RegexValidator(
        regex='^[a-zA-Z0-9]+$',
    )])
    passwd = models.CharField(
        max_length=16,
        validators=[MinLengthValidator(8), MaxLengthValidator(16), validators.RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,16}$')]
    )
    email = models.EmailField(unique=True)


    def __str__(self):
        return f"{self.username}, {self.email}, {self.passwd}"
    
class Usuarios(models.Model):
    username = models.CharField(max_length=16, unique=True, validators=[validators.RegexValidator(
        regex='^[a-zA-Z0-9]+$',
    )])
    passwd = models.CharField(max_length=16, validators=[MinLengthValidator(8), MaxLengthValidator(16)])
    email = models.EmailField(unique=True)


    def __str__(self):
        return f"{self.username}, {self.email}, {self.passwd}"

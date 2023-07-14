from django.db import models

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="Profesional", null=True)

    def __str__(self):
        return self.nombre
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre + " "+self.email


Aceptada = [
    [0, "Aceptada"],
    [1, "--------"]
]
Rechazada = [
    [0, "Rechazada"],
    [1, "--------"]
]


class Atencion(models.Model):
    numero = models.IntegerField()
    nombre = models.ForeignKey(Profesional, on_delete=models.PROTECT)
    diagnóstico = models.TextField()
    materiales = models.TextField()
    foto = models.ImageField(upload_to="Profesional", null=True)
    Aceptada = models.IntegerField(choices=Aceptada, null=True)
    Rechazada = models.IntegerField(choices=Rechazada, null=True)
    motivoRechazo = models.TextField(null=True)


    def __str__(self):
        return self.numero
    

class curriculum(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    Informacion_profecional = models.TextField()
    datosDeContacto = models.TextField()
    foto = models.ImageField(upload_to="Profesional", null=True)

    def __str__(self):
        return self.rut    
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    mis_profesionales = Profesional.objects.all()

    data = {
        "profesionales" : mis_profesionales
    }
    
    return render(request, "index.html", data)

def login(request):
    return render(request, "login.html")

def menuAdmin(request):
    return render(request, "menuAdmin.html")

def menuMecanico(request):
    return render(request, "menuMecanico.html")

def contacto(request):

    data = {
        'miForm': ContactoForm
    }

    if request.method == "POST":
        formulario = ContactoForm(data = request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado!!!"
        else:
            data['mensaje'] = "Hubo un problema"
            data['miForm'] = formulario

    return render(request, "contacto.html", data)



def agregarMecanico(request):

    data={
        'form': MecanicoForm
    }

    if request.method == "POST":
        formulario = MecanicoForm(data = request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mecanico Agregado!!!"
        else:
            data['mensaje'] = "Hubo un problema"
            data['MecanicoForm'] = formulario

    return render(request, "mantenedor/mecanico/agregar.html", data)



def agregarAtencion(request):

    data={
        'atencionForm': AtencionForm
    }

    if request.method == "POST":
        formulario = AtencionForm(data = request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Atencion Creada!!!"
        else:
            data['mensaje'] = "Hubo un problema"
            data['atencionForm'] = formulario


    return render(request, "mantenedor/atencion/agregar.html", data)

def listarMecanico(request):

    mis_profesionales = Profesional.objects.all()

    data = {
        "profesionales" : mis_profesionales
    }

    
    return render(request, "mantenedor/mecanico/listar.html", data)


def listarAtencion(request):

    mis_Atencion = Atencion.objects.all()

    data = {
        "Atencion" : mis_Atencion
    }

    return render(request, "mantenedor/atencion/listar.html",data)

def listarAtencionAprovadas(request):

    mis_Atencion = Atencion.objects.all()

    data = {
        "Atencion" : mis_Atencion
    }

    return render(request, "mantenedor/atencion/listarAprovados.html",data)

def listarAtencionRechazadas(request):

    mis_Atencion = Atencion.objects.all()

    data = {
        "Atencion" : mis_Atencion
    }

    return render(request, "mantenedor/atencion/listarRechazados.html",data)

def modificar_Atecion(request, numero_atencion):

    atencion = get_object_or_404(Atencion, numero=numero_atencion)

    data = {
        'form' : AtencionForm(instance= atencion)
    }

    if request.method == 'POST':
        formulario = AtencionForm(data=request.POST, files=request.FILES, instance=atencion)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_atencion")
        else:
            data["mensaje"] = "No se puede guardar"
            data["form"] = formulario

    return render(request, 'mantenedor/Atencion/modificar.html', data)


def eliminar_Atecion(request, numero_atencion):

    atencion = get_object_or_404(Atencion, numero=numero_atencion)

    atencion.delete()

           
    return redirect(to="listar_atencion")



def rechazo(request, numero_atencion):

    atencion = get_object_or_404(Atencion, numero=numero_atencion)

    data = {
        'form' : AtencionForm2(instance= atencion)
    }

    if request.method == 'POST':
        formulario = AtencionForm2(data=request.POST, files=request.FILES, instance=atencion)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarAtencionRechazadas")
        else:
            data["mensaje"] = "No se puede guardar"
            data["form"] = formulario

    return render(request, 'mantenedor/Atencion/rechazo.html', data)


def aprovado(request, numero_atencion):

    atencion = get_object_or_404(Atencion, numero=numero_atencion)

    data = {
        'form' : AtencionForm3(instance= atencion)
    }

    if request.method == 'POST':
        formulario = AtencionForm3(data=request.POST, files=request.FILES, instance=atencion)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarAtencionAprovadas")
        else:
            data["mensaje"] = "No se puede guardar"
            data["form"] = formulario

    return render(request, 'mantenedor/Atencion/aprovado.html', data)


def login_usuario(request):



    return redirect(to='home')



def registro(request):

    data = {
        "mensaje" : ""
    }

    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            data["mensaje"] = "Las contraseñas deben ser identicas"
        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = nombre
            usu.first_name = nombre
            usu.last_name = apellido
            grupo = Group.objects.get(name='mecanico')
            try:
                usu.save()
                usu.groups.add(grupo)
                data["mensaje"] = "Usuario creado"

                user = authenticate(username=usu.username, password=password1)
                login(request, user)
                return redirect(to='home')

            except:
                data["mensaje"] = "Hubo un error"

    return render(request, "registration/registro.html")


def saber_mas(request, Nombre):

    atencion = get_object_or_404(Profesional, nombre=Nombre)

    mis_Atencion = Atencion.objects.all()

    data = {
        "Atencion" : mis_Atencion,
        "nombre " : atencion
    }

    return render(request, "mantenedor/atencion/saberMas.html",data)

def agregarCurriculum(request):

    data={
        'curriculumForm': CurriculumForm
    }

    if request.method == "POST":
        formulario = CurriculumForm(data = request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Atencion Creada!!!"
        else:
            data['mensaje'] = "Hubo un problema"
            data['CurriculumForm'] = formulario


    return render(request, "mantenedor/curriculum/agregar.html", data)


def listarCurriculum(request):

    mis_Curriculums = curriculum.objects.all()

    data = {
        "Curriculum" : mis_Curriculums
    }

    return render(request, "mantenedor/curriculum/listar.html",data)

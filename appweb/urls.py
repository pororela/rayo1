from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('menuAdmin/', menuAdmin, name="menuAdmin"),
    path('menuMecanico/', menuMecanico, name="menuMecanico"),
    path('contacto/', contacto, name="contacto"),
    path('mantenedor/agregar_mecanico/',agregarMecanico, name="agregar_mecanico"),
    path('mantenedor/listar_mecanico/',listarMecanico, name="listar_mecanico"),
    path('mantenedor/agregar_atencion/',agregarAtencion, name="agregar_atencion"),
    path('mantenedor/listar_atencion/',listarAtencion, name="listar_atencion"),
    path('mantenedor/listarAtencionAprovadas/',listarAtencionAprovadas, name="listarAtencionAprovadas"),
    path('mantenedor/listarAtencionRechazadas/',listarAtencionRechazadas, name="listarAtencionRechazadas"),
    path('mantenedor/modificar_atencion/<numero_atencion>/',modificar_Atecion, name="modificar_Atecion"),
    path('mantenedor/eliminar_Atecion/<numero_atencion>/',eliminar_Atecion, name="eliminar_Atecion"),
    path('mantenedor/rechazo/<numero_atencion>/',rechazo, name="rechazo"),
    path('mantenedor/aprovado/<numero_atencion>/',aprovado, name="aprovado"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('mantenedor/saber_mas/<Nombre>/',saber_mas, name="saber_mas"),
    path('mantenedor/agregar_curriculum/',agregarCurriculum, name="agregar_curriculum"),
    path('mantenedor/listar_curriculum/',listarCurriculum, name="listar_curriculum"),
]



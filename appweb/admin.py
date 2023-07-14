from django.contrib import admin
from .models import *

#class ContactoAdmin(admin.ModelAdmin):
class profesionalAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre']
    list_editable = ['nombre']
    search_fields = ['rut']
    

admin.site.register(Cargo)
admin.site.register(Profesional, profesionalAdmin)
admin.site.register(Contacto)
admin.site.register(Atencion)
admin.site.register(curriculum)
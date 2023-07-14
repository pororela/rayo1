from django import forms
from .models import *

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"

class MecanicoForm(forms.ModelForm):

    class Meta:
        model = Profesional
        fields = "__all__"       

        widgets = {
            "fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        } 

class AtencionForm(forms.ModelForm):

    class Meta:
        model = Atencion
        fields = ["numero","nombre","diagnóstico","materiales","foto"]        

class AtencionForm2(forms.ModelForm):

    class Meta:
        model = Atencion
        fields = ["Rechazada","motivoRechazo"]              

class AtencionForm3(forms.ModelForm):

    class Meta:
        model = Atencion
        fields = ["Aceptada"]              

class CurriculumForm(forms.ModelForm):

    class Meta:
        model = curriculum
        fields = "__all__"       

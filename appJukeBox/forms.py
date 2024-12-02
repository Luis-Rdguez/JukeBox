# appJukeBox/forms.py
from django import forms
from .models import *

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nombre', 'descripcion', 'pais', 'fechaIni', 'fechaFin', 'foto', 'estilos']
        
        widgets = {
            'fechaIni': forms.DateInput(attrs={'type': 'date'}),
            'fechaFin': forms.DateInput(attrs={'type': 'date'}),
            'estilos': forms.SelectMultiple(attrs={
                'class': 'form-control',  # Clase para estilizarlo con Bootstrap o CSS
                'placeholder': 'Selecciona estilos'
            }),
            'foto': forms.URLInput(attrs={
                'class': 'form-control',  # Clase para estilizar el campo URL
                'placeholder': 'URL de la foto'
            })
        }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['pais', 'bandera']  # Ajusta los campos según tu modelo
        widgets = {
            'bandera': forms.URLInput(attrs={'placeholder': 'URL de la bandera'}),
        }

class EstiloForm(forms.ModelForm):
    bandas = forms.ModelMultipleChoiceField(
        queryset=Banda.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',  # Clase estándar de Bootstrap o personalizada para estilos básicos
        }),
        required=False
    )

    class Meta:
        model = Estilo
        fields = ['estilo', 'descripcion', 'bandas']
        widgets = {
            'estilo': forms.TextInput(attrs={
                'placeholder': 'Nombre del estilo',  # Placeholder para el nombre del estilo
                'class': 'form-control'  # Clase estándar para inputs
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Descripción del estilo',
                'rows': 3,
                'class': 'form-control'  # Estilo estándar para textarea
            }),
            
        }

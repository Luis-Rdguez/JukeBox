# appJukeBox/forms.py
from django import forms
from .models import *

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nombre', 'descripcion', 'pais', 'fechaIni', 'fechaFin', 'foto', 'estilos']
        
        # Personaliza los widgets si es necesario
        widgets = {
            'fechaIni': forms.DateInput(attrs={'type': 'date'}),
            'fechaFin': forms.DateInput(attrs={'type': 'date'}),
            'estilos': forms.CheckboxSelectMultiple(),  # Para seleccionar varios estilos
            'foto': forms.URLInput()
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
            'class': 'select2',  # Clase select2 para el buscador
            'data-placeholder': 'Selecciona bandas relacionadas',
        }),
        required=False
    )

    class Meta:
        model = Estilo
        fields = ['estilo', 'descripcion', 'bandas']
        widgets = {
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción del estilo', 'rows': 3}),
        }
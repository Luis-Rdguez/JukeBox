# appJukeBox/forms.py
from django import forms
from .models import Banda

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

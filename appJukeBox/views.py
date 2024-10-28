from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *
# Create your views here.

#devuelve el listado de empresas
def index_pais(request):
	pais = get_list_or_404(Pais.objects.order_by('nombre'))
	context = {'lista_paiss': pais }
	return render(request, 'index.html', context) # TODO cambiar el html

#devuelve los datos de un departamento
def show_pais(request, pais_id):
	pais = get_object_or_404(Pais, pk=pais_id)
	context = {'pais': pais } 
	return render(request, 'detail.html', context)

#devuelve los empelados de un departamento
def index_bandas(request, pais_id):
	pais = get_object_or_404(Pais, pk=pais_id)
	bandas =  pais.banda_set.all()
	context = {'Pais': pais, 'Bandas' : bandas }
	return render(request, 'empleados.html', context) # TODO cambiar el html

#devuelve los detalles de un empleado
def show_banda(request, banda_id):
	banda = get_object_or_404(Banda, pk=banda_id)
	estilos =  banda.estilos.all()
	context = { 'banda': banda, 'estilos' : estilos }
	return render(request, 'empleado.html', context) # TODO cambiar el html

# Devuelve los detalles de una habilidad
def show_estilo(request, estilo_id):
    estilo = get_object_or_404(Estilo, pk=estilo_id)
    bandas =  estilo.banda_set.all()
    context = { 'Bandas': bandas, 'estilo' : estilo }
    return render(request, 'habilidad.html', context) # TODO cambiar el html
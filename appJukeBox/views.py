from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *
# Create your views here.

def index(request):
	return render(request, 'index.html')

# Devuelve el listado de bandas
def index_pais(request):
	pais = get_list_or_404(Pais.objects.order_by('nombre'))
	context = {'lista_pais': pais }
	return render(request, 'index.html', context) # TODO cambiar el html

# Devuelve los datos de un pais
def show_pais(request, pais_id):
	pais = get_object_or_404(Pais, pk=pais_id)
	context = {'pais': pais } 
	return render(request, 'index.html', context) # TODO cambiar el html

# Devuelve las bandas de un pais
def index_bandas(request, pais_id):
	pais = get_object_or_404(Pais, pk=pais_id)
	bandas =  pais.banda_set.all()
	context = {'pais': pais, 'bandas' : bandas }
	return render(request, 'blog.html', context) # TODO cambiar el html

# Devuelve los detalles de una banda
def show_banda(request, banda_id):
	banda = get_object_or_404(Banda, pk=banda_id)
	estilos =  banda.estilos.all()
	context = { 'banda': banda, 'estilos' : estilos }
	return render(request, 'blog.html', context) # TODO cambiar el html

# Devuelve los detalles de una habilidad
def show_estilo(request, estilo_id):
    estilo = get_object_or_404(Estilo, pk=estilo_id)
    bandas =  estilo.banda_set.all()
    context = { 'bandas': bandas, 'estilo' : estilo }
    return render(request, 'blog.html', context) # TODO cambiar el html
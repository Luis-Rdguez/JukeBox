from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Pais, Banda, Estilo

# Página de inicio: Muestra una banda destacada por país
def index(request):
    bandas_por_pais = []
    for pais in Pais.objects.all():
        banda = Banda.objects.filter(pais=pais).order_by('fechaIni').first()
        if banda:
            bandas_por_pais.append(banda)
    context = {'bandas_por_pais': bandas_por_pais}
    return render(request, 'index.html', context)

# Página de inicio: Muestra una banda destacada por país
def show_bandas(request):
    bandas = []
    for banda in Banda.objects.all():
        bandas.append(banda)
    context = {'bandas': bandas}
    return render(request, 'track.html', context)

# Listado de todos los países, incluyendo el número de bandas de cada país
def index_pais(request):
    paises = Pais.objects.all().order_by('pais')
    context = {
        'lista_pais': [
            {
                'pais': pais,
                'numero_bandas': pais.numero_bandas(),
            }
            for pais in paises
        ]
    }
    return render(request, 'track.html', context)

# Detalle de un país: incluye todas las bandas de ese país y el conteo de bandas
# En views.py
def show_pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    bandas = pais.banda_set.all()
    context = {
        'pais': pais,
        'bandas': bandas,  # Se pasa la queryset directamente para asegurar el acceso a 'id'
        'numero_bandas': bandas.count(),

    }
    return render(request, 'pais.html', context)


# Listado de bandas de un país específico
def index_bandas(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    bandas = pais.banda_set.all()
    context = {
        'pais': pais,
        'bandas': [
            {
                'nombre': banda.nombre,
                'descripcion': banda.descripcion,
                'fechaIni': banda.fechaIni,
                'fechaFin': banda.fechaFin,
                'estilos': banda.estilos.all(),
            }
            for banda in bandas
        ],
        'numero_bandas': pais.numero_bandas(),
    }
    return render(request, 'track.html', context)

# Detalle de una banda, incluyendo país de origen y estilos
def show_banda(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)
    context = {
        'banda': {
            'nombre': banda.nombre,
            'descripcion': banda.descripcion,
            'fechaIni': banda.fechaIni,
            'fechaFin': banda.fechaFin,
            'pais': banda.pais,
            'estilos': banda.estilos.all(),
        },
        'pais': banda.pais,
        'estilos': banda.estilos.all(),
    }
    return render(request, 'banda.html', context)

# Detalle de un estilo musical: incluye las bandas asociadas y el número total de bandas en ese estilo
def show_estilo(request, estilo_id):
    estilo = get_object_or_404(Estilo, pk=estilo_id)
    bandas = estilo.banda_set.all()
    context = {
        'estilo': estilo,
        'bandas': [
            {
                'nombre': banda.nombre,
                'descripcion': banda.descripcion,
                'fechaIni': banda.fechaIni,
                'fechaFin': banda.fechaFin,
                'pais': banda.pais,
            }
            for banda in bandas
        ],
        'numero_bandas': estilo.numero_bandas(),
    }
    return render(request, 'index.html', context)

# Listado de todos los estilos, incluyendo el número de bandas de cada estilo
def show_estilos(request):
    estilos = []
    for estilo in Estilo.objects.all():
        estilos.append(estilo) 
    context = {'estilos': estilos }
    return render(request, 'estilos.html', context)
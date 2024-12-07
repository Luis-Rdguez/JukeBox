from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse  # Para generar URLs dinámicamente
from .models import *
from .forms import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate
from urllib.parse import urlparse

# Página de inicio: Muestra una banda destacada por país
def index(request):
    bandas_por_pais = []
    paises = get_list_or_404(Pais)
    for pais in paises:
        banda = Banda.objects.filter(pais=pais).order_by('fechaIni').first()
        if banda:
            bandas_por_pais.append(banda)
    context = {
        'bandas_por_pais': bandas_por_pais,
        'titulo': _("Página de inicio"),  # Texto estático traducible
        }
    return render(request, 'index.html', context)

# Página de inicio: Muestra una banda destacada por país
def show_bandas(request):
    bandas = get_list_or_404(Banda)
    context = {'bandas': bandas}
    return render(request, 'bandas.html', context)

# Listado de todos los países, incluyendo el número de bandas de cada país
def index_pais(request):
    paises = get_list_or_404(Pais.objects.all().order_by('pais'))
    context = {
        'lista_pais': [
            {
                'pais': pais,
                'numero_bandas': pais.numero_bandas(),
            }
            for pais in paises
        ]
    }
    return render(request, 'bandas.html', context)

# Detalle de un país: incluye todas las bandas de ese país y el conteo de bandas
def show_pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)

    # Intentar obtener las bandas asociadas a este país
    bandas = pais.banda_set.all()

    # Si no hay bandas, pasar un mensaje especial
    if not bandas:
        no_bandas_message = _("No hay bandas creadas para este país.")

    # Preparar el contexto para pasar a la plantilla
    context = {
        'pais': pais,
        'bandera': pais.bandera,
        'bandas': bandas,
        'numero_bandas': len(bandas),
        'no_bandas_message': no_bandas_message if not bandas else None,  # Mensaje si no hay bandas
    }

    # Renderizar la plantilla
    return render(request, 'pais.html', context)


# Listado de bandas de un país específico
def index_bandas(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    bandas = get_list_or_404(pais.banda_set.all())
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
    return render(request, 'bandas.html', context)

# Detalle de una banda, incluyendo país de origen y estilos
def show_banda(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)
    context = {
        'banda': {
            'foto': banda.foto,
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
    bandas = get_list_or_404(estilo.banda_set.all())  # Obtener todas las bandas que tienen el estilo actual
    context = {
        'estilo': estilo,
        'bandas': bandas,  # Pasar las bandas directamente en el contexto
        'descripcion' : estilo.descripcion,
        'numero_bandas': len(bandas),  # Contar el número de bandas en este estilo
    }
    return render(request, 'estilo.html', context)

# Listado de todos los estilos, incluyendo el número de bandas de cada estilo
def show_estilos(request):
    estilos = get_list_or_404(Estilo)
    context = {'estilos': estilos }
    return render(request, 'estilos.html', context)

def show_paises(request):
    # Obtiene todos los países y el total de bandas
    paises = get_list_or_404(Pais)
    total_bandas = Banda.objects.count()

    # Construye una lista de diccionarios con datos calculados por cada país
    paises_info = []
    for pais in paises:
        numero_bandas = pais.numero_bandas()  # Usa el método 'numero_bandas' del modelo
        # Calcula el porcentaje de bandas en el país con respecto al total
        porcentaje = (numero_bandas / total_bandas * 100) if total_bandas > 0 else 0
        paises_info.append({
            'pais': pais,
            'numero_bandas': numero_bandas,
            'porcentaje': porcentaje,
        })

    # Pasa los datos al contexto
    context = {
        'paises_info': paises_info,
    }
    return render(request, 'paises.html', context)


def add_banda(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            banda = form.save(commit=False)  # Guarda la banda sin los campos ManyToMany
            banda.save()  # Guarda la banda en la base de datos
            form.save_m2m()  # Guarda los campos ManyToMany (estilos)
            
            # Redirigir a la página de descripción de la banda recién creada
            return redirect(reverse('banda', args=[banda.id]))
    else:
        form = BandaForm()

    return render(request, 'addBanda.html', {'form': form})


def add_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            pais = form.save()  # Guarda el país en la base de datos
            return redirect(reverse('pais', args=[pais.id]))
    else:
        form = PaisForm()

    return render(request, 'addPais.html', {'form': form})

def add_estilo(request):
    if request.method == 'POST':
        form = EstiloForm(request.POST)
        if form.is_valid():
            # Crear el objeto Estilo pero aún no guardarlo en la base de datos
            estilo = form.save(commit=False)

            # Si quieres realizar algún procesamiento antes de guardar, puedes hacerlo aquí
            # No necesitas generar un código, ya que lo has eliminado del modelo

            estilo.save()  # Ahora guardamos el estilo en la base de datos

            # Obtener las bandas seleccionadas del formulario
            bandas_seleccionadas = form.cleaned_data['bandas']

            # Asociar las bandas seleccionadas al estilo recién creado
            for banda in bandas_seleccionadas:
                banda.estilos.add(estilo)  # Usamos el método `add()` para agregar el estilo a cada banda

            # Redirigir a la vista de detalle del estilo
            return redirect(reverse('estilo', args=[estilo.id]))  # Asumimos que la vista detalle se accede por id del estilo
    else:
        form = EstiloForm()

    return render(request, 'addEstilo.html', {'form': form})

def switch_language(request, lang_code):
    """
    Cambia el idioma del sitio y redirige a la URL adecuada.
    """
    # Obtener la referencia anterior o usar la raíz como predeterminada
    referer = request.META.get('HTTP_REFERER', '/')
    parsed_url = urlparse(referer)
    path = parsed_url.path  # Extrae solo el path (sin dominio)

    current_lang = get_language()

    # Remover el prefijo actual del idioma
    if path.startswith(f"/{current_lang}/"):
        path = path[len(f"/{current_lang}/"):]
    elif path.startswith(f"/{current_lang}"):
        path = path[len(f"/{current_lang}"):]

    # Garantizar que la ruta tenga el formato adecuado
    if not path.startswith('/'):
        path = '/' + path

    # Activar el nuevo idioma y redirigir
    activate(lang_code)
    return redirect(f"/{lang_code}{path}")

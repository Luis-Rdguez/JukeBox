from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    #path('admin/', admin.site.urls), # TODO
    path('', views.index, name='index'), # Esto funciona en index y te muestra una banda por pais
    path('bandas/', views.show_bandas, name='todas_bandas'),   # Esto funciona en track y te muestra todas las bandas
    path('paises/', views.show_paises, name='todos_paises'),   # Esto funciona en track y te muestra todos los paises
    path('paises/<int:pais_id>/', views.show_pais, name='pais'),
    path('bandas/<int:banda_id>/', views.show_banda, name='banda'),
    path('estilos/<int:estilo_id>/', views.show_estilo, name='estilo'),
    path('estilos/', views.show_estilos, name='todos_estilos'), # Esto funciona en estiloso y te muestra todos los estilos
    path('add/', views.add_banda, name='addBanda'),  # URL para agregar una nueva banda

]

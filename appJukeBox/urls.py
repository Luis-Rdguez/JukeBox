from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    #path('admin/', admin.site.urls), # TODO
    path('', views.index, name='index'), # Esto funciona en index y te muestra una banda por pais
    path('bandas/', views.show_bandas, name='todas_bandas'),   # Esto funciona en track y te muestra todas las bandas
    path('paises/<int:pais_id>/', views.show_pais, name='detail'),
    path('paises/<int:pais_id>/bandas', views.index_bandas, name='bandas'),
    path('bandas/<int:banda_id>/', views.show_banda, name='banda'),
    path('estilos/<int:estilo_id>', views.show_estilo, name='estilo'),
]

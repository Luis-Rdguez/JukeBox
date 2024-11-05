from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    #path('admin/', admin.site.urls), # TODO
    path('', views.index, name='index'),
    path('paises/<int:pais_id>/', views.show_pais, name='detail'),
    path('paises/<int:pais_id>/bandas', views.index_bandas, name='bandas'),
    path('bandas/<int:banda_id>', views.show_banda, name='banda'),
    path('estilos/<int:estilo_id>', views.show_estilo, name='estilo'),
]

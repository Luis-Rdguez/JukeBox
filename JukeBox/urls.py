"""
URL configuration for JukeBox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Ruta para cambiar el idioma (necesaria para el formulario de selección de idioma)
    path('i18n/', include('django.conf.urls.i18n')),
]

# Añadimos las rutas principales con soporte para el prefijo de idioma
urlpatterns += i18n_patterns(
    path('', include('appJukeBox.urls')),  # Tu app principal
    path('admin/', admin.site.urls),       # Panel de administración
    prefix_default_language=True,         # Opcional: sin prefijo para el idioma por defecto
)
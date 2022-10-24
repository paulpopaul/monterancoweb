"""monterancoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('artistas/', TemplateView.as_view(template_name="artistas.html"), name='artistas'),
    path('sesiones/', TemplateView.as_view(template_name="sesiones.html"), name='sesiones'),
    path('salas/', TemplateView.as_view(template_name="salas.html"), name='salas'),
    path('servicios/', TemplateView.as_view(template_name="servicios.html"), name='servicios'),
    path('fichatecnica/', TemplateView.as_view(template_name="fichatecnica.html"), name='fichatecnica'),
    path('contacto/', TemplateView.as_view(template_name="contacto.html"), name='contacto'),
] 

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
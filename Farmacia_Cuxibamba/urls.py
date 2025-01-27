"""
URL configuration for Farmacia_Cuxibamba project.

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
from django.views.generic import TemplateView
from django.urls import path
from Farmacia.views import registrar_usuario, home_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('', home_view, name='root'),
    path('empleado/', TemplateView.as_view(template_name='empleado.html'), name='empleados'),
    path('cliente/', TemplateView.as_view(template_name='cliente.html'), name='clientes'),
]
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Gym import views
from Gym.views import index, agregar_bebida, agregar_clase, agregar_entrenador, buscar_bebida, buscar, busquedaBebida, mostrar_bebida, mostrar_otro

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path('agregar/bebida/',agregar_bebida, name="agregar/bebida/" ),
    path('agregar/entrenador/', agregar_entrenador, name= 'agregar/entrenador/'),
    path('agregar/clase/', agregar_clase, name='agregar/clase/'),
    path("buscar/", busquedaBebida, name= 'buscar/'),
    path('resultado/', buscar,name= 'resultado/'),
    path('buscar_bebida', buscar_bebida, name= 'buscar_bebida'),
    path('mostrar/bebida/', mostrar_bebida, name='mostrar/bebida/'),
    path('mostrar/otro/', mostrar_otro, name= 'mostrar/otro/'),
]

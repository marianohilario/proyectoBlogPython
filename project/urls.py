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
from blogcab.views import index, PostListar, PostCrear, PostDetalle, PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogcab/', index, name="blogcab-index"),
    path('blogcab/<int:pk>/detalle/', PostDetalle.as_view(), name="blogcab-detalle"),
    path('blogcab/listar/', PostListar.as_view(), name="blogcab-listar"),
    path('blogcab/crear/', PostCrear.as_view(), name="blogcab-crear"),
    path('blogcab/<int:pk>/borrar/', PostBorrar.as_view(), name="blogcab-borrar"),
    path('blogcab/<int:pk>/actualizar/', PostActualizar.as_view(), name="blogcab-actualizar"),
    path('blogcab/signup/', UserSignUp.as_view(), name="blogcab-signup"),
    path('blogcab/login/', UserLogin.as_view(), name="blogcab-login"),
    path('blogcab/logout/', UserLogout.as_view(), name="blogcab-logout"),
]

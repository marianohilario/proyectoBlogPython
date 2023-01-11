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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blogcab.views import index, PostListar, PostCrear, PostDetalle, PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, MensajeBorrar, about

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
    path('blogcab/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="blogcab-avatars-actualizar"),
    path('blogcab/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="blogcab-users-actualizar"),
    path('blogcab/mensajes/crear/', MensajeCrear.as_view(), name="blogcab-mensajes-crear"),
    path('blogcab/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="blogcab-mensajes-detalle"),
    path('blogcab/mensajes/listar/', MensajeListar.as_view(), name="blogcab-mensajes-listar"),
    path('blogcab/mensaje/<int:pk>/borrar/', MensajeBorrar.as_view(), name="blogcab-mensajes-borrar"),
    path('blogcab/about', about, name="blogcab-about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
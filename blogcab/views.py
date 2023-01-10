from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from blogcab.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from blogcab.forms import UsuarioForm

def index(request):
  return render(request, "blogcab/index.html", {})

class PostDetalle(DetailView):
  model = Post

class PostListar(ListView):
  model = Post

class PostCrear(LoginRequiredMixin, CreateView):
  model = Post
  success_url = reverse_lazy("blogcab-listar")
  fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = reverse_lazy("blogcab-listar")

class PostActualizar(UpdateView):
  model = Post
  success_url = reverse_lazy("blogcab-listar")
  fields = '__all__'

class UserSignUp(CreateView):
  form_class = UsuarioForm
  template_name = 'registration/signup.html'
  success_url = reverse_lazy("blogcab-listar")

class UserLogin(LoginView):
  next_page = reverse_lazy("blogcab-listar")

class UserLogout(LogoutView):
  next_page = reverse_lazy("blogcab-index")
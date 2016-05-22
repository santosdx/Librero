from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Libro

# Create your views here.

def home(request):
    usuario = request.user
    context = {'usuario': usuario,}
    return render(request, 'libro/index.html', context)

#@login_required(login_url="/admin/login/")
def welcome(request):
    titulo = 'Aplicación de libros'
    saludo = 'Bienvenidos a la aplicación para la gestión de libros, creada y diseñada desde el Framework Django mediante lenguaje Python. '
    context = {
        'titulo': titulo,
        'saludo': saludo,
        'error_mensaje': "Error en la página",
    }
    return render(request, 'libro/welcome.html', context)

def about(request):
    autor = 'Santiago Rojas Manios'
    context = {
        'autor': autor,
        'error_mensaje': "Error en la página",
    }
    return render(request, 'libro/about.html', context)

@method_decorator(login_required(login_url="/admin/login/"), name='dispatch')
class DetailView(generic.DetailView):
    model = Libro
    template_name = 'libro/detail.html'

@method_decorator(login_required(login_url="/admin/login/"), name='dispatch')
class ListView(generic.ListView):
    #model = Libro
    template_name = 'libro/list.html'
    """
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        return context """

    def get_queryset(self):
        """Retorna la lista de libros ordenados por el atributo nombre"""
        return Libro.objects.order_by('nombre')
"""Librero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from . import views

app_name = 'libro'
urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^about/', views.about, name='about'),
    #url(r'^/(?P<pk>[0-9]+)/detail', views.DetailView.as_view(), name='detail'), #Otra forma de mostrar el detalle
    url(r'^(?P<pk>[0-9]+)/detail', views.DetailView.as_view(), name='detail'),
    url(r'^list/', views.ListView.as_view(), name='list'),
    #url(r'^list/', login_required(views.ListView.as_view(template_name='list'))),
]

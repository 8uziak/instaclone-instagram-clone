"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path 
from . import views 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('category.html', views.category, name="category"),
    path('products.html', views.products, name="products"),
    path('clients.html', views.clients, name="clients"),
    path('contact.html', views.contact, name="contact"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('styles/favicon.ico'))),
]

from django.shortcuts import render

def index(request):
    return render(request, 'index.html',{})

def category(request):
    return render(request, 'category.html',{})

def products(request):
    return render(request, 'products.html',{})

def clients(request):
    return render(request, 'clients.html',{})

def contact(request):
    return render(request, 'contact.html',{})


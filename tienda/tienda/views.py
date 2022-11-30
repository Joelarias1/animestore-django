from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from animestore.models import Product, imageProduct

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    return render(request, "register.html")

def products(request):

    return render(request, "products.html")


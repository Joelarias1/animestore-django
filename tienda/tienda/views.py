from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from animestore.models import Product, imageProduct, category, contactUs
from animestore.forms import newCommentForm
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):  
    form = newCommentForm()
    if request.method == 'POST':
        form = newCommentForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {"form": newCommentForm()}
    return render(request, "contact.html", context)


def register(request):
    return render(request, "register.html")

def products(request):
    total_categories = category.objects.all().count()
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products.html", context)


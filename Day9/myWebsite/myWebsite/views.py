from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from newApp.models import Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponse("Contact")
def services(request):
    return HttpResponse("Services")

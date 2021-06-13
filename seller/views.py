from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'seller/Home.html')


def About(request):
    return render(request, 'seller/About.html')
    
def details(request):
    return render(request, 'seller/Details.html')
    
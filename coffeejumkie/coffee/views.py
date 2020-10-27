from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    pros = Products.objects.all()
    return render(request,'index.html',{'pros':pros})


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def numbers(request):
    return render(request,'numbers.html')
from django.shortcuts import render
from . import views
# Create your views here.

def home(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')

def list(request):
    return render(request,'list.html')

# def add2(request):
#     return render(request,'add2.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')


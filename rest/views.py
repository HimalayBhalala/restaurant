from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'rest/home.html')

def book(request):
    return render(request,'rest/book.html')

def about(request):
    return render(request,'rest/about.html')

def menu(request):
    return render(request,'rest/menu.html')

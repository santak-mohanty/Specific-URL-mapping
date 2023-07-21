from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1>This is the first view of app1</h1>")

def second(request):
    return HttpResponse("<h1>This is the second view of app1</h1>")

    

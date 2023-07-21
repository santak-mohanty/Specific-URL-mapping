from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse("<h1>This is the first view of app2")

def second(request):
    return HttpResponse("<h1>This is the second view of app2</h1>")
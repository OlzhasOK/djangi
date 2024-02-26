from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is your home view.")
def index(request):
    return HttpResponse('<h1>Hello World!<h1>')
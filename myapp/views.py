from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Homepage</h1>")
def about(request):
    return HttpResponse("<h2>About page</h2>")
def service(request):
    return HttpResponse("<h1>Service</h1>")
def contact(request):
    return HttpResponse("<h1>Contact</h1>")
def index(request):
    return HttpResponse("<h1>index</h1>")
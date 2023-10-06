from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def wish(request):
    return  HttpResponse("<h1>Wellcome to Django class </h1>")
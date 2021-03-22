from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requeest):
    return HttpResponse("App is Working")



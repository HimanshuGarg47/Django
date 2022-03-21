from django.shortcuts import render
from django.http import HttpResponse , Http404  , HttpResponseRedirect , HttpResponseNotFound
from django.urls import reverse
import datetime

# Create your views here.

def index(request):
    return render(request, 'Home/index.html' , {})

def contact(request):
    pass


def home(request):
    return render(request, 'Home/home.html',{})
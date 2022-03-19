from django.shortcuts import render
from django.http import HttpResponse , Http404  , HttpResponseRedirect , HttpResponseNotFound
from django.urls import reverse
from Home.models import Student
import datetime

# Create your views here.

def index(request):
    return render(request,'Home/index.html')

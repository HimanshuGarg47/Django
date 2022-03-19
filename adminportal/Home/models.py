from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse



# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=10)
    textbox = models.TextField(max_length=200)
    
    
    def __str__(self) -> str:
        return self.name + " " + self.email
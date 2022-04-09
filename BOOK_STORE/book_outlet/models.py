from tkinter import CASCADE
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
    def __str__(self):
        return self.full_name()
    
    
class Book(models.Model):
    title = models.CharField( max_length=50)
    rating  = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author , on_delete= models.CASCADE , null = True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    
    def __str__(self):
        return f"{self.title} ({self.rating} ) [{self.is_bestselling}]"
    
    
    # def save(self, *args , **kwargs):
    #     self.slug = slugify(self.title)   #  slugify(' Joel is a slug ')  'joel-is-a-slug'
    #     super().save(*args, **kwargs)
        
        
        
    
    

    
from pickle import FALSE
from django.db import models
from django.utils import timezone
# Create your models here.
from wsgiref.validate import validator
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify
from datetime import date

from pyparsing import null_debug_action
from zmq import NULL

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,default="")
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Tag(models.Model):
    caption = models.CharField(max_length=20, unique=True)
    
    
    def __str__(self):
        return self.caption
    
class Posts(models.Model):
    
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    author =  models.ForeignKey(Author, on_delete=models.CASCADE, blank=FALSE) 
    tagline = models.ManyToManyField(Tag) 
    pub_date = models.DateField()    
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    
    
    class Meta:
        verbose_name_plural = "Posts"
        
        
    def save(self, *args , **kwargs):
        # self.slug = slugify(self.title)
        #  slugify(' Joel is a slug ')  'joel-is-a-slug'
        self.date = date.today()
        super().save(*args, **kwargs)

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE , related_name="comments")
    
    
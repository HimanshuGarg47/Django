from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField( max_length=50)
    rating  = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    
    def __str__(self):
        return f"{self.title} ({self.rating} ) [{self.is_bestselling}]"
    
    
    def save(self, *args , **kwargs):
        self.slug = slugify(self.title)   #  slugify(' Joel is a slug ')  'joel-is-a-slug'
        super().save(*args, **kwargs)
        
        
        
    
    

    
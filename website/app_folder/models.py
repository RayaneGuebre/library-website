from django.db import models
from django.utils.text import slugify
import isbnlib 


# Create your models here.

class Category( models.Model): 
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it’s empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs) 
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    is_available = models.BooleanField(default=True)
    isbn= models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/', max_length=255, blank=True)
    def __str__(self):
        return self.name                                        
class FeaturedBooks(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()  # To order the featured books
    
    def __str__(self):
        return f"{self.book.name} - Featured"


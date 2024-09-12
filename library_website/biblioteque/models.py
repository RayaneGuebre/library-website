from django.db import models

# Create your models here.

class Category( models.Model): 
    name = models.charField(max_lenght=255, unique=True)
    description = models.textField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class book(models.Model):
    name = models.CharField(max_lenght=255)
    author = models.chaarField(max_lenght=255)
    publication_date = models.DateField()
    isbn= models.CharField(max_lenght=255, unique=True)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='covers/')                                        
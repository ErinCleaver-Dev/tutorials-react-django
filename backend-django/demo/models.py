from django.db import models

# How to create models
#first you create a class in python.

#django documentation:  https://docs.djangoproject.com/en/3.2/ref/models/fields/
class Book(models.Model):
    #then you add fields to the book class
    #create a new object that has a title
    #to apply the changes you run: python3 manage.py makemigrations
    #to apply the mirgation run: python3 manage.py migrate
    title = models.CharField(blank=False, max_length=100, unique=True)
    description = models.TextField(blank=True, max_length=256)

    price = models.DecimalField(default=0, max_digits=3,  decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.FileField(upload_to='cover/', blank=True)
    
from django.db import models

# How to create models
#first you create a class in python.
class Book(models.Model):
    #then you add fields to the book class
    #create a new object that has a title
    #to apply the changes you run: python3 manage.py makemigrations
    #to apply the mirgation run: python3 manage.py migrate
    title = models.CharField(max_length=36)

from django.db import models

# How to create models
#first you create a class in python.

#use case of one to one 
#one to one means each book will only have one realtion ship
#used to extend the model
#creating an new class called book number
#each book has its own ISBN, this is a unique number and cannot be repeated
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


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
    
    #You add a one to one field
    #Add the class name to the one to one field
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


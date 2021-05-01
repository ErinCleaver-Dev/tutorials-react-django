# add a seiralizer.py file

from rest_framework import serializers;
#import the class to serializer that you would like to serialize
from .models import Book

#then create a class for the Serializer
class BookSerializer(serializers.ModelSerializer):
    #add a Meta class:
    class Meta:
        # use the model for book
        model = Book
        # tell django that what fields to display using the model
        fields = ['title']        

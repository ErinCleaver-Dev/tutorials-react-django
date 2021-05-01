# add a seiralizer.py file

from rest_framework import serializers;
#import the class to serializer that you would like to serialize
from .models import Book, BookNumber

class BookNumberSerializer(serializers.ModelSerializer):
    #add Meta class:
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']

#then create a class for the Serializer
class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    #add a Meta class:
    class Meta:
        # use the model for book
        model = Book
        # tell django that what fields to display using the model
        fields = ['title', 'description', 'price', 'published', 'cover', 'is_published', 'number']        

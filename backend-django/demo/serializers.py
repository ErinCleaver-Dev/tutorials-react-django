# add a seiralizer.py file

from rest_framework import serializers;
#import the class to serializer that you would like to serialize
from .models import Book, BookNumber, Character, Author

class BookNumberSerializer(serializers.ModelSerializer):
    #add Meta class:
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']

# added a serializer for Characters
class CharacterSerializer(serializers.ModelSerializer):
    #add Meta class:
    class Meta:
        model = Character
        fields = ['id', 'name']

#added an serializer for Author
class AuthorSerializer(serializers.ModelSerializer):
    #add Meta class:
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']

#then create a class for the Serializer
class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = CharacterSerializer(many=True)

    #add a Meta class:
    class Meta:
        # use the model for book
        model = Book
        # tell django that what fields to display using the model
        fields = ['id','title', 'description', 'price', 'published', 'cover', 'is_published', 'number', 'characters', 'authors']        

class BookMiniSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = CharacterSerializer(many=True)

    #add a Meta class:
    class Meta:
        # use the model for book
        model = Book
        # tell django that what fields to display using the model
        fields = ['id', 'title']        

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):

    # gets all of the objects from book and places them in books
    books = Book.objects.all();

    if (len(books) == 1):
        output = f"We have { len(books) } book in Database."

    else:
        output = f"We have { len(books) } that many books in Database."


    def get(self, request):
        return HttpResponse(self.output)
# Create your views here.


def first(request):
    return HttpResponse('First Message from Views')
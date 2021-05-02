from rest_framework import viewsets
# import the serializers
from .serializers import BookSerializer, BookMiniSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

"""def first(request):
    books = Book.objects.all();
    #to pass in agurements type in {}
    return render(request, 'first_temp.html', {'books': books})
"""


#clreated a view set for books 
class BooksViewSet(viewsets.ModelViewSet):
    # Tells what serializer we want to use
    serializer_class = BookMiniSerializer
    #then make a qqurey set for the view
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes =(IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


"""class Another(View):

    # gets all of the objects from book and places them in books
    books = Book.objects.filter();
    output = ''

    book = Book.objects.get(id=1);

    if (len(books) == 1):
        output += f"We have {book.title} books in the Database with ID {book.id}.<br>"
        output +=f"The price is {book.price}<br>"
        output += f"We have { len(books) } book in the Database."
    else:
        for book in books:
            output += f"We have {book.title} books in the Database with ID {book.id}.<br>"
            output +=f"The price is {book.price}<br>"
        
        output += f"We have { len(book) } books in the Database."


    def get(self, request):
        return HttpResponse(self.output)
# Create your views here.


def first(request):
    return HttpResponse('First Message from Views')"""
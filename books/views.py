from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def book_list(request):
    """
    returns all published books in :model: 'books.Book' and displays them in a 
    page of 9 books.

    **Context**

    ``books``
        A queryset of all published books in the database.

    **Template**

    :template:`books/book_list.html`
    """

    books = Book.objects.filter(status=1)

    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context)
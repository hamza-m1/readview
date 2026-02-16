from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Book

# Create your views here.


def book_list(request):
    """
    returns all published books in :model: 'books.Book' and displays them in a 
    page of 6 books.

    **Context**

    ``books``
        A queryset of all published books in the database.

    **Template**

    :template:`books/index.html`
    """

    books = Book.objects.filter(status=1).order_by('-publication_date')

    paginator = Paginator(books, 6)  # Show 6 books per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'books': books,
        'page_obj': page_obj

    }
    return render(request, 'books/index.html', context)
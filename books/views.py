from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Book
from .forms import ReviewForm

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

def book_detail(request, slug):
    """
    Display a single :model: 'books.Book'.

    **Context**

    ``book``
        A single book object from :model: 'books.Book' that matches the slug.

    **Template**

    :template:`books/detail.html`
    """

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)

    reviews = book.reviews.all().order_by('-posted_on')
    reviews_count = book.reviews.filter(approved=True).count()

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.reviewer = request.user
            new_review.book = book
            new_review.save()

    review_form = ReviewForm()

    context = {
        'book': book,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'review_form': review_form,
    }
    return render(request, 'books/book_detail.html', context)
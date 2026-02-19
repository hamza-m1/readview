from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Book, Review, Genre
from .forms import ReviewForm, RequestBookForm

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
    genres = Genre.objects.all()

    if request.method == 'POST' and 'search_query' in request.POST:
        search_query = request.POST.get('search_query', '')
        books = books.filter(title__icontains=search_query) | books.filter(author__icontains=search_query)
    elif request.method == 'POST' and 'genre_filter' in request.POST:
        genre_filter = request.POST.get('genre_filter', '')
        books = books.filter(genre__name=genre_filter)

    paginator = Paginator(books, 6)  # Show 6 books per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'books': books,
        'page_obj': page_obj,
        'genres': genres,
    }
    return render(request, 'books/index.html', context)


def book_detail(request, slug):
    """
    Display a single :model: 'books.Book'.

    **Context**

    ``book``
        A single book object from :model: 'books.Book' that matches the slug.

    **Template**

    :template:`books/book_detail.html`
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
            messages.add_message(
                request,
                messages.SUCCESS,
                'Review submitted successfully, awaiting approval.'
                )
    review_form = ReviewForm()

    context = {
        'book': book,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'review_form': review_form,
    }
    return render(request, 'books/book_detail.html', context)


def review_edit(request, slug, review_id):
    """
    Edit a review for a book.

    **Context**

    ``review``
        A single review object from :model: 'books.Review' that matches the review_id.

    **Template**

    :template:`books/book_detail.html`
    """

    if request.method == "POST":

        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.reviewer == request.user:
            review = review_form.save(commit=False)
            review.book = book
            review.approved = False
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review updated successfully. Thanks for sharing.'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating review. Please try again.'
            )

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    Delete a review for a book.

    **Context**

    ``review``
        A single review object from :model: 'books.Review' that matches the review_id.

    **Template**

    :template:`books/book_detail.html`
    """

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted. Thanks for contributing.')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


def request_book(request):
    """
    Allow users to request a book to be added to the database.

    **Context**

    ``form``
        A form for users to request a book to be added to the database.

    **Template**

    :template:`books/request_book.html`
    """

    if request.method == 'POST':
        form = RequestBookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.status = 2
            new_book.save()
            form.save_m2m()
            messages.add_message(
                request, messages.SUCCESS,
                'Book request submitted successfully. Thanks for contributing.'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error submitting book request. Please try again.'
            )
    form = RequestBookForm()

    context = {
        'form': form,
    }
    return render(request, 'books/request_book.html', context)

from django.contrib import admin
from .models import Book, Genre, Review, Favourite
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status')
    list_filter = ('status', 'publication_date')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('summary',)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('book', 'reviewer', 'approved', 'posted_on')
    list_filter = ('approved', 'posted_on', 'book')
    search_fields = ('reviewer',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')

# Register your models here.

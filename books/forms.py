from .models import Review, Book
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }


class RequestBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']
        widgets = {
            'genre': forms.CheckboxSelectMultiple(),
        }

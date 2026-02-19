from .models import Review, Book
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your review here...'}),
            'rating': forms.Select(choices=[(i, f"{i} Stars") for i in range(6)]),
        }


class RequestBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']
        widgets = {
            'genre': forms.CheckboxSelectMultiple(),
        }

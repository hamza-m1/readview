from .models import Review, Book
from django import forms


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, user=None, book=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.book = book

    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 8, 'placeholder': 'Write your review here...'}
            ),
            'rating': forms.Select(
                choices=[(i, f"{i} Stars") for i in range(6)]
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        user = self.user
        book = self.book

        if user and user.is_authenticated and book:
            existing_review = Review.objects.filter(reviewer=user, book=book)

            if self.instance and self.instance.pk:
                existing_review = existing_review.exclude(pk=self.instance.pk)

            if existing_review.exists():
                raise forms.ValidationError(
                    "You have already reviewed this book."
                )

        return cleaned_data


class RequestBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']
        widgets = {
            'genre': forms.CheckboxSelectMultiple(),
        }

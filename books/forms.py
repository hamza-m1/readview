from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

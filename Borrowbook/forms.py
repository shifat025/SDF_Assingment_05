from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        # labels = {
        #     'rating': 'Rating',
        #     'comment': 'Comment',
        # }
        # widgets = {
        #     'rating': forms.Select(choices=Review.RATING_CHOICES, attrs={'class': 'form-control'}),
        #     'comment': forms.Textarea(attrs={'class': 'form-control'}),
        # }
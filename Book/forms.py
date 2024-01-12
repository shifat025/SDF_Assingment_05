from django import forms
from .models import Books,Book_category

class Book_form(forms.ModelForm):
    class Meta:
        model = Books
        fields = '--all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Book_category
        fields = '__all__'

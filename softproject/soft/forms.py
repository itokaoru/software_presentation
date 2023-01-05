from django import forms
from .models import Book,Review

class BookForm(forms.Models):
    class Meta:
        model=Book
        fields=['title','text','thumbnail','map','user']
        widgets={'user':forms.HiddenInput()}

class ReviewForm(forms.Models):
    class Meta:
        model=Review
        fields=['book','title','text','rate','user']
        widgets={'user':forms.HiddenInput()}

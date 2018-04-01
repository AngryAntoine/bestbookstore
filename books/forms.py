from django import forms
# from datetime import date
from .models import (Book)


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title',
                  'authors',
                  'publish_date',
                  'image',
                  'isbn',
                  'price',
                  ]

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     book_exists = Book.objects.filter(title__iexact=title).exists()
    #     if book_exists:
    #         raise forms.ValidationError('Book with this title already exists')
    #     return title

from django import forms
from .models import Books

class BooksForm(forms.Form):
    class Meta:
        model = Books
        field = ['name', 'author', 'description', 'image']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 300:
            raise forms.ValidationError('This is too long')
        return description

from django import forms
from django.forms import DateInput

from webapp.models import Author, Book, FavoriteBook, Genre, Review


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = (
            "first_name",
            "second_name",
        )


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            "title",
            "author",
            "genre",
            "description"
        )


class FavoriteForm(forms.ModelForm):

    class Meta:
        model = FavoriteBook
        fields = (
            "book",
        )


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = (
            "name",
        )


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            "rating",
            "text"
        )


class BookFilterForm(forms.Form):

    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    date_from = forms.DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(required=False, widget=DateInput(attrs={'type': 'date'}))


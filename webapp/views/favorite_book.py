from django.shortcuts import get_object_or_404, redirect
from django.views import View
from webapp.models import Book, FavoriteBook
from django.contrib.auth.mixins import LoginRequiredMixin


class ToggleFavoriteBookView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        favorite, created = FavoriteBook.objects.get_or_create(user=request.user, book=book)

        if not created:
            favorite.delete()

        return redirect('index')

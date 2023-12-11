from django.views.generic import ListView

from webapp.forms import BookFilterForm
from webapp.models import Book, FavoriteBook


class IndexView(ListView):
    context_object_name = "books"
    model = Book
    template_name = "index.html"
    ordering = ["-created_at"]
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        form = BookFilterForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data["genre"]:
                queryset = queryset.filter(genre=form.cleaned_data["genre"])
            if form.cleaned_data["author"]:
                queryset = queryset.filter(author=form.cleaned_data["author"])
            if form.cleaned_data["date_from"]:
                queryset = queryset.filter(
                    created_at__gte=form.cleaned_data["date_from"]
                )
            if form.cleaned_data["date_to"]:
                queryset = queryset.filter(
                    created_at__lte=form.cleaned_data["date_to"]
                )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = BookFilterForm(self.request.GET)
        if self.request.user.is_authenticated:
            favorite_books_ids = FavoriteBook.objects.filter(
                user=self.request.user
            ).values_list("book_id", flat=True)
            context["favorite_books_ids"] = favorite_books_ids

        return context

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import BookForm
from webapp.models import Book


class BookCreateView(CreateView):
    template_name = "book_create.html"
    model = Book
    form_class = BookForm
    success_message = "Book is added."

    def get_success_url(self):
        return reverse("book_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        book = form.save(commit=False)
        book.save()
        return super().form_valid(form)


class BookDetail(DetailView):
    template_name = "book_detail_view.html"
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        reviews = book.review_set.all()
        context["reviews"] = reviews
        return context


class BookUpdateView(UpdateView):
    template_name = "book_update.html"
    model = Book
    form_class = BookForm
    success_message = "Book is updated"

    def get_success_url(self):
        return reverse("book_detail", kwargs={"pk": self.object.pk})


class BookDeleteView(DeleteView):
    template_name = "book_confirm_delete.html"
    model = Book
    success_url = reverse_lazy("index")
    success_message = "Book is deleted."

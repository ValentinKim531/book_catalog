from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Book


class ReviewDetail(DetailView):
    template_name = "review_detail_view.html"
    model = Review
    context_object_name = "review"


class BookReviewCreateView(CreateView):
    template_name = "review_create.html"
    model = Review
    form_class = ReviewForm
    success_message = "Review is added."

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        review = form.save(commit=False)
        review.book = book
        review.user = self.request.user
        review.save()
        book.update_average_rating()
        return redirect("book_detail", pk=book.pk)


class BookReviewUpdateView(UpdateView):
    model = Review
    template_name = "review_update.html"
    form_class = ReviewForm
    context_object_name = "review"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.book.update_average_rating()
        return response

    def get_success_url(self):
        return reverse("review_detail", kwargs={"pk": self.object.pk})


class BookReviewDeleteView(DeleteView):
    template_name = "review_confirm_delete.html"
    model = Review
    success_url = reverse_lazy("index")

    def form_valid(self, request, *args, **kwargs):
        review = self.get_object()
        book = review.book
        response = super().delete(request, *args, **kwargs)
        book.update_average_rating()
        return response

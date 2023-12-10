from django.urls import path

from webapp.views.base import IndexView
from webapp.views.books import BookCreateView, BookUpdateView, BookDetail, BookDeleteView
from webapp.views.favorite_book import ToggleFavoriteBookView
from webapp.views.review import ReviewDetail, BookReviewCreateView, BookReviewDeleteView, BookReviewUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("book/<int:pk>", BookDetail.as_view(), name="book_detail"),
    path("book/add", BookCreateView.as_view(), name="book_add"),
    path("book/<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    path("book/<int:pk>/delete/", BookDeleteView.as_view(), name="book_confirm_delete"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="review_detail"),
    path("review/<int:pk>/add/", BookReviewCreateView.as_view(), name="review_add"),
    path("review/<int:pk>/update/", BookReviewUpdateView.as_view(), name="review_update"),
    path("review/<int:pk>/delete/", BookReviewDeleteView.as_view(), name="review_confirm_delete"),
    path('book/<int:pk>/toggle-favorite/', ToggleFavoriteBookView.as_view(), name='toggle_favorite_book'),
]

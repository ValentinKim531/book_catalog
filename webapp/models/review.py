from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

from .book import Book


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
            MinValueValidator(1, message="Рейтинг не может быть меньше 1"),
            MaxValueValidator(5, message="Рейтинг не может быть больше 5")
        ])
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


from django.db import models
from .author import Author
from .genre import Genre


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='books')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


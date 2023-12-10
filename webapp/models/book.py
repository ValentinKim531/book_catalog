from django.db import models
from django.utils import timezone

from .author import Author
from .genre import Genre


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='books')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_deleted = models.BooleanField(
        verbose_name="удалено", null=False, default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None,
    )
    average_rating = models.FloatField(default=0.0, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def update_average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            average = reviews.aggregate(models.Avg('rating'))['rating__avg']
            self.average_rating = round(average, 2)
        else:
            self.average_rating = 0
        self.save()

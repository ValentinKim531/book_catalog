from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.second_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
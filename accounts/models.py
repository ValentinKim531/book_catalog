from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта", unique=True, blank=True
    )
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.viewsets import (
    BookViewSet,
    AuthorViewSet,
    GenreViewSet,
    FavoriteBookViewSet,
    ReviewViewSet,
    AccountViewSet,
)

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"favorite_books", FavoriteBookViewSet)
router.register(r"reviews", ReviewViewSet)
router.register(r"accounts", AccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

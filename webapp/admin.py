from django.contrib import admin
from webapp.models import Author, Book, FavoriteBook, Genre, Review


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "second_name",
    )
    list_filter = ("id", "first_name", "second_name")
    search_fields = ("second_name",)
    fields = ("first_name", "second_name")
    readonly_fields = ("id",)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "display_genre",
        "description",
        "created_at"
    )
    list_filter = ("id", "title", "author", "genre", "created_at")
    search_fields = ("title", "author")
    fields = ("id", "title", "author", "description", "genre")
    readonly_fields = ("id",)

    def display_genre(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])

    display_genre.short_description = "Genre"


class FavoriteBookAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "book"
    )
    list_filter = ("id", "user", "book")
    search_fields = ("user", "book")
    fields = ("id", "user", "book")
    readonly_fields = ("id",)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    list_filter = ("id", "name")
    search_fields = ("name",)
    fields = ("id", "name")
    readonly_fields = ("id",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "user",
        "rating",
        "text"
    )
    list_filter = ("id", "book", "user", "rating")
    search_fields = ("book", "user", "rating")
    fields = ("id", "book", "user", "rating", "text")
    readonly_fields = ("id",)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(FavoriteBook, FavoriteBookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)


from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "second_name")
    list_filter = ("id", "email", "first_name", "second_name")
    search_fields = ("email", "first_name", "second_name")
    fields = ("email", "first_name", "second_name")
    readonly_fields = ("id",)


admin.site.register(Account, AccountAdmin)

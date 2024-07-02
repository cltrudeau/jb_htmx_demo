from django.contrib import admin

from books.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "last_name", "first_name")

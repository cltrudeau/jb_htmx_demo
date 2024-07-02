import time

from books.models import Book
from django.shortcuts import render


def home(request):
    data = {
        "books": Book.objects.all(),
    }

    return render(request, "home.html", data)


def lazy_page(request):
    return render(request, "lazy.html")


def lazy_image(request):
    time.sleep(2)
    return render(request, "snippets/lazy_image.html")

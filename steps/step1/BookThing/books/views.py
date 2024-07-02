from books.models import Book
from django.shortcuts import render


def home(request):
    data = {
        "books": Book.objects.all(),
    }

    return render(request, "home.html", data)

from django.shortcuts import render

from books.models import Book

def home(request):
    data = {
        "books": Book.objects.all(),
    }

    return render(request, "home.html", data)

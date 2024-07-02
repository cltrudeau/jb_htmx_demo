import time #@= 2-
from django.shortcuts import render

from books.models import Book

def home(request):
    data = {
        "books": Book.objects.all(),
    }

    return render(request, "home.html", data)
#@[ 2-


def lazy_page(request):
    return render(request, "lazy.html")


def lazy_image(request):
    time.sleep(2)
    return render(request, "snippets/lazy_image.html")
#@]

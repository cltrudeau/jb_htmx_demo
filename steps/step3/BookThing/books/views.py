import time
import urllib

from books.models import Book
from django.core.paginator import Paginator
from django.db.models import Q
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


def search(request):
    search_text = request.GET.get("search_text", "")
    search_text = urllib.parse.unquote(search_text)

    books = []

    if search_text:
        parts = search_text.split()
        q = (
            Q(first_name__startswith=parts[0])
            | Q(last_name__startswith=parts[0])
            | Q(title__startswith=parts[0])
        )

        for part in parts[1:]:
            q |= (
                Q(first_name__startswith=part)
                | Q(last_name__startswith=part)
                | Q(title__startswith=part)
            )

        books = Book.objects.filter(q)

    paginator = Paginator(books, 2)
    page_num = int(request.GET.get("page", 1))
    page = paginator.page(page_num)

    data = {
        "search_text": search_text,
        "books": page.object_list,
        "has_more": page.has_next(),
        "next_page": page_num + 1,
    }

    return render(request, "search.html", data)

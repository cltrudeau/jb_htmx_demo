import time #@= 2-
import urllib #@= 3-
from django.core.paginator import Paginator #@= 3-
from django.db.models import Q #@= 3-
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
#@[ 3-
def search(request):
    search_text = request.GET.get("search_text", "")
    search_text = urllib.parse.unquote(search_text)

    books = []

    if search_text:
        parts = search_text.split()
        q = Q(first_name__startswith=parts[0]) | \
            Q(last_name__startswith=parts[0]) | \
            Q(title__startswith=parts[0])

        for part in parts[1:]:
            q |= Q(first_name__startswith=part) | \
                Q(last_name__startswith=part) | \
                Q(title__startswith=part)

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

#@[ 4-
    if request.htmx:
        if page_num > 1:
            time.sleep(2)

        return render(request, "snippets/search_results.html", data)

#@]
    return render(request, "search.html", data)
#@]

from django.contrib import admin
from django.urls import path

from books import views as book_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', book_views.home, name="home"),
]

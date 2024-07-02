from django.contrib import admin
from django.urls import path

from books import views as book_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', book_views.home, name="home"),
    path('lazy_page/', book_views.lazy_page, name="lazy_page"), #@= 2-
    path('lazy_image/', book_views.lazy_image, name="lazy_image"), #@= 2-
]

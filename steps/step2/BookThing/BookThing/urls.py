from books import views as book_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", book_views.home, name="home"),
    path("lazy_page/", book_views.lazy_page, name="lazy_page"),
    path("lazy_image/", book_views.lazy_image, name="lazy_image"),
]

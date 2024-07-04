from django.db import models
from django.utils.text import Truncator


class Book(models.Model):
    title = models.CharField(max_length=50)
    libthing_id = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Book(title={self.short_title}"

    @property
    def short_title(self):
        return Truncator(self.title).chars(15, truncate="...")

    @property
    def image(self):
        return f"img/{self.libthing_id}.jpg"

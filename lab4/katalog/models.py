from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    author = models.CharField(max_length=100, verbose_name="Autor")
    description = models.TextField(blank=True, verbose_name="Opis")
    published_year = models.IntegerField(verbose_name="Rok wydania")
    is_available = models.BooleanField(default=True, verbose_name="Dostępna")

    def __str__(self):
        return f"{self.title} - {self.author}"
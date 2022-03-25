from django.db import models

# Create your models here.
class Author(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    mobile = models.CharField(max_length=15, null=False, blank=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}"


class Book(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=128, null=False, blank=False)
    authors = models.ManyToManyField(Author, related_name="books_authors")

    def __str__(self) -> str:
        return f"{self.name}"

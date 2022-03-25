from dataclasses import fields
import django_filters
from django_filters import CharFilter
from books.models import Author


class AuthorFilter(django_filters.FilterSet):
    name = CharFilter(method="name_filter")

    def name_filter(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "email",
            "mobile",
        ]

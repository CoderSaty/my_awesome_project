from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from books.models import Author, Book
from books.serializers import BookSerializer, AuthorSerializer
from books.filters import AuthorFilter

# python core library
# django lib
# external lib
# local packages


def author_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    # if request.method == 'GET':
    author = Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    return JsonResponse(serializer.data, safe=False)


def book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    # if request.method == 'GET':
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return JsonResponse(serializer.data, safe=False)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.order_by("id")
    serializer_class = AuthorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AuthorFilter
    permission_classes = ()

    def get_queryset(self):
        queryset = Author.objects.filter(is_verified=True).order_by("id")

        return queryset


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by("id")
    serializer_class = BookSerializer
    permission_classes = ()

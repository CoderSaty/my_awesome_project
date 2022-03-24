from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Author,Book 
from .serializers import BookSerializer,AuthorSerializer
from rest_framework import viewsets

def author_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    #if request.method == 'GET':
    author = Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    return JsonResponse(serializer.data, safe=False)


def book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    #if request.method == 'GET':
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return JsonResponse(serializer.data, safe=False)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.order_by("id")
    serializer_class = AuthorSerializer
    permission_classes =()
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by("id")
    serializer_class = BookSerializer
    permission_classes =()
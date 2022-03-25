#from msilib.schema import Class
from rest_framework import serializers
from .models import Author,Book

class AuthorSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    
    class Meta:
        model = Author
        fields = ['id', 'name','email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'address','authors']

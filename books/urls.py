from django.urls import path
from books import views

urlpatterns = [
    path('authors/', views.author_list),
    path('books/', views.book_list),
]
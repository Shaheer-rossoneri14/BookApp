from django.shortcuts import render 
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Book, Author, Genre
# Create your views here.

class BooksListView(generic.ListView):
    model = Book
    template_name = 'list.html'

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'language']
    

    
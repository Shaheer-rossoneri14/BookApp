from django.shortcuts import redirect
from django.urls import path
from .views import BooksListView
from . import views

urlpatterns = [
    path('', BooksListView.as_view(), name = 'list'),
    path('App', views.BookCreate.as_view(),name='book-create'),
]
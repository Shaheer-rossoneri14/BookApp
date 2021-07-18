from django.db import models
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, Poetry etc.)")

    def __str__(self):
        return self.name

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)

class Book(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.CharField('Author', max_length=200, default='')
    genre = models.ManyToManyField('Genre', max_length= 20, help_text="Hold 'Ctrl' button to select multiple", default='null')
    language = models.CharField(max_length=100, default='')
    
    def get_absolute_url(self):
        return reverse('list')

    def __str__(self):
        return self.title
   
        
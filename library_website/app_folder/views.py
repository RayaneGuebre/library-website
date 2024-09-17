from django.shortcuts import render, get_object_or_404
from .models import Category, Book

def home(request):
    categories = Category.objects.all()
    return render(request, 'app_folder/home.html', {'categories': categories})

def books_in_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    books = category.books.all()  # Using the related_name 'books' from the ForeignKey in the Book model
    return render(request, 'app_folder/category.html', {'category': category, 'books': books})

def book_detail(request, book_name):
    book = get_object_or_404(Book, name=book_name)
    return render(request, 'app_folder/book_detail.html', {'book': book})

import os
from django.shortcuts import render, get_object_or_404
from .models import Category, Book, FeaturedBooks
import requests
from dotenv import load_dotenv
load_dotenv()


def home(request):
    categories = Category.objects.all()
    specific_books = Book.objects.filter(name__in=["The Lord of the Rings", "Harry Potter", "Wonder"])
    return render(request, 'app_folder/home.html', {
        'categories': categories,
        'specific_books': specific_books})

def books_in_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    books = category.books.all()  # Using the related_name 'books' from the ForeignKey in the Book model
    return render(request, 'app_folder/category.html', {'category': category, 'books': books})

def book_detail(request, book_slug, category_name):
    
    category = get_object_or_404(Category, name=category_name)
    book = get_object_or_404(Book, slug=book_slug)
    isbn = book.isbn
    api_key = os.getenv("GOOGLE_BOOKS_API_KEY")
    cover_url = None
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        if "items" in data:
            cover_url = data["items"][0]["volumeInfo"].get("imageLinks", {}).get("thumbnail")
            if cover_url:
                cover_url = cover_url.replace("zoom=1", "zoom=2").replace("zoom=2", "zoom=3")
    else: 
        print("Failed to find the cover")
    
    return render(request, 'app_folder/book_detail.html', {'book': book,'cover_url' : cover_url})


def homepage_view(request):
    featured_books = FeaturedBooks.objects.order_by('order')[:3]  # Adjust this to show only 3 books
    context = {'featured_books': featured_books}
    return render(request, 'homepage.html', context)

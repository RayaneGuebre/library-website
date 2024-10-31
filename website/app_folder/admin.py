from django.contrib import admin
from .models import Category, Book
from .models import FeaturedBooks

admin.site.register(FeaturedBooks)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display these fields in the list view

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publication_date', 'is_available', 'isbn', 'category', 'is_available')

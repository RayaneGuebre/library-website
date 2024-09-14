from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),  # Home page showing all categories
    path('<str:name>/', views.books_by_category, name='books_by_category'),  # Page for books in a specific category
    path('<str:category_name>/<str:book_name>/', views.book_detail, name='book_detail'),  # Page for a specific book
]
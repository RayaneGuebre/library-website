from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='category_list'),  # Home page showing all categories
    path('<str:category_name>/', views.books_in_category, name='books_in_category'),
    path('<str:category_name>/<str:book_name>/', views.book_detail, name='book_detail'),  # Page for a specific book
]
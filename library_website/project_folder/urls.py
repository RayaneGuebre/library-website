from django.contrib import admin
from django.urls import path, include  # include allows you to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('biblioteque.urls')),  # Include the URLs from your 'biblioteque' app
    path('', views.category_list, name='category_list'),  # Home page that lists all categories
    path('<str:name>/', views.books_by_category, name='books_by_category'),  # URL for each category by name
]

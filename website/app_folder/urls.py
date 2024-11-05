from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='category_list'),  # Home page showing all categories
    path('<str:category_name>/', views.books_in_category, name='books_in_category'),
    path('<str:category_name>/<slug:book_slug>/', views.book_detail, name='book_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
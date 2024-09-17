from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Route to the admin interface
    path('', include('app_folder.urls')),
 # Route to the biblioteque app's URLs
]


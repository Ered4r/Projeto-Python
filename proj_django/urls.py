from django.contrib import admin
from django.urls import path, include
from login import views  # Import views from the login app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),  # Include login app URLs
    path('', views.home, name='home'),  # Home page (root URL)
]
from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page (root URL)
    path('login/', views.login_view, name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
    path('criar_pessoa/', views.criar_pessoa, name='criar_pessoa'),  # Create user
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),  # List users
]
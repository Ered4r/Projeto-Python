from django.urls import path
from . import views

urlpatterns = [
    path('criar_pessoa/', views.criar_pessoa, name='criar_pessoa'),
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),
]
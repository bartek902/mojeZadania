from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/obiekty/', views.api_books, name='api_books'),
]
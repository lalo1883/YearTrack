from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('add/', views.add, name='add'),
    path('weekly/', views.weekly, name='weekly'),
]
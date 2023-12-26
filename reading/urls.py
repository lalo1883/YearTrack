from django.urls import path
from . import views

urlpatterns = [

    path('', views.books, name='books'),
    path('add/', views.add, name='add'),
    path('weekly/', views.weekly, name='weekly'),
    path('delete/<int:entry_id>/', views.remove_book, name='remove_book'),
    path('delete_description/<int:entry_id>/', views.remove_description, name='remove_description'),

]
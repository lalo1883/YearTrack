from django.urls import path

from . import views

urlpatterns = [
    path('', views.gym_track_view, name='gym'),
    path('delete/<int:entry_id>/', views.delete_gym_entry, name='delete_gym_entry'),

]
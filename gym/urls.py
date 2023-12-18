from django.urls import path

from . import views

urlpatterns = [
    path('', views.gym_track_view, name='gym'),
]
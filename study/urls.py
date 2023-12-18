from django.urls import path


from . import views

urlpatterns = [
    path('', views.study, name='study'),
    path('add_study/', views.add_study, name='add_study'),
    path('weekly_add/', views.weekly_add, name='weekly_add'),
]
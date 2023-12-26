from django.urls import path


from . import views

urlpatterns = [
    path('', views.study, name='study'),
    path('add_study/', views.add_study, name='add_study'),
    path('weekly_add/', views.weekly_add, name='weekly_add'),
    path('remove_course/<int:entry_id>/', views.remove_course, name='remove_course'),
    path('remove_reflections/<int:entry_id>/', views.remove_reflections, name='remove_reflections'),
]
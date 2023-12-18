from django.forms import ModelForm
from .models import Books, weekly_track


class BooksForm(ModelForm):
    class Meta:
        model = Books

        fields = ['name', 'topic', 'author', 'status', 'rating', 'pages']


class weekly_trackForm(ModelForm):
    class Meta:
        model = weekly_track
        fields = ['hours_read', 'pages_read', 'reflexions']
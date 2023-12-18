from django.forms import ModelForm

from .models import Courses, weekly_track

class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

class weekly_trackForm(ModelForm):
    class Meta:
        model = weekly_track
        fields = '__all__'


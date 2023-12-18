from .models import gym_track
from django import forms

class gym_track_form(forms.ModelForm):
    class Meta:
        model = gym_track
        fields = '__all__'
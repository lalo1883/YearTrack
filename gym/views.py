from django.shortcuts import render
from .models import gym_track
from .forms import gym_track_form


# Create your views here.

def gym_track_view(request):
    form = gym_track_form()
    data = gym_track.objects.all()

    # Get the total hours trained
    total_hours = 0
    total_days = 0
    for i in data:
        total_hours += i.trained_hours
        total_days += i.trained_days


    if request.method == 'POST':
        form = gym_track_form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form, 'data': data, 'total_hours': total_hours, 'total_days': total_days}

    return render(request, 'gym.html', context)

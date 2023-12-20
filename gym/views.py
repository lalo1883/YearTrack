from django.shortcuts import render, get_object_or_404, redirect
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

    if request.method == 'DELETE':
        form = gym_track_form(request.DELETE)
        if form.is_valid():
            form.delete()

    return render(request, 'gym.html', context)


def delete_gym_entry(request, entry_id):
    entry = get_object_or_404(gym_track, id=entry_id)
    entry.delete()
    return redirect('gym')
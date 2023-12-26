from django.shortcuts import render, get_object_or_404, redirect
from .models import Courses, weekly_track
from .forms import CoursesForm, weekly_trackForm


# Create your views here.


def study(request):
    study_data = Courses.objects.all()
    weeklt_data = weekly_track.objects.all()
    context = {'study_data': study_data, 'weeklt_data': weeklt_data}
    return render(request, 'study.html', context)


def add_study(request):
    form = CoursesForm()
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'add_course.html', context)


def weekly_add(request):
    form = weekly_trackForm()
    if request.method == 'POST':
        form = weekly_trackForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'week_add.html', context)



def remove_course(request, entry_id):
    entry = get_object_or_404(Courses, id=entry_id)
    entry.delete()
    return redirect('study')

def remove_reflections(request, entry_id):
    entry = get_object_or_404(weekly_track, id=entry_id)
    entry.delete()
    return redirect('study')
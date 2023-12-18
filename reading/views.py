from django.shortcuts import render
from .models import Books, weekly_track
from .forms import BooksForm, weekly_trackForm

# Create your views here.

def books(request):
    data = Books.objects.all()
    week_data = weekly_track.objects.all()
    return render(request, 'books.html', {'data': data, 'week_data': week_data})

def add(request):
    form = BooksForm()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'add.html', context)


def weekly (request):
    form_w = weekly_trackForm()
    if request.method == 'POST':
        form_w = weekly_trackForm(request.POST)
        if form_w.is_valid():
            form_w.save()
    context = {'form_w': form_w}
    return render(request, template_name='weekly.html', context=context)

from django.shortcuts import render
from django.views import View
from showcatalog.models import Show


# Create your views here.


def index(request):
    return render(request, 'showcatalog/index.html')


def about(request):
    return render(request, 'showcatalog/about.html')


def dashboard(request):
    shows = Show.objects.raw("SELECT * FROM showcatalog_show ORDER BY id ASC;")

    context = {
        'shows': shows
    }
    return render(request, 'showcatalog/dashboard.html', context)


def update_show_page(request):
    return render(request, 'showcatalog/update_show.html')


def add_show_page(request):
    return render(request, 'showcatalog/add_show.html')

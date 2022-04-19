import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def get_content(file):
    with open(file, newline='') as csvfile:
        return list(csv.DictReader(csvfile))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(get_content("data-398-2018-08-30.csv"), 10)
    stations = paginator.get_page(page_number)
    context = {
            'bus_stations': stations,
            'page': stations,
    }
    return render(request, 'stations/index.html', context)

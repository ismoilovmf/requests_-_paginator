from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


path = "../pagination/data-398-2018-08-30.csv"

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        list_bus_stations = list(reader)
    paginator = Paginator(list_bus_stations, 20)
    page_num = int(request.GET.get('page', 1))
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

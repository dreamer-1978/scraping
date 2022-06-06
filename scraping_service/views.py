from django.shortcuts import render
import datetime


def home(request):
    data = datetime.datetime.now().date()
    name = 'Serega'
    cont = {
        'name': name,
        'data': data,
    }
    return render(request, 'home.html', cont)
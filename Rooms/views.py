from django.conf import settings
from decimal import Decimal
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Rooms.models import room

# Create your views here.

# def room(request):
#     return render(request, 'suru/room.html')

def roomdisplay(request):
    roomdisplay = room.objects.all()
    return render(request, 'suru/room.html', {'room': roomdisplay})

def payment(request):
    return render(request, 'suru/payment.html')


def checkout(request, pk):
	Room = room.objects.get(id=pk)
	context = {'Room':Room}
	return render(request, 'base/checkout.html', context)


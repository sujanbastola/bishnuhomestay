from django.shortcuts import render
from gallery.models import imggal

# Create your views here.


def imagedisplay(request):
    resultsdisplay = imggal.objects.all()
    return render(request, 'suru/gallery.html', {'imggal': resultsdisplay})
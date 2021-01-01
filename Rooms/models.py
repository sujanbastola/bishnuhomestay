from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError("Date cannot be in the past")

from datetime import datetime


# Create your models here.
class room(models.Model):
    roomtitle = models.CharField(max_length=100)
    roomno = models.CharField(max_length=400)
    price = models.CharField(max_length=20)
    availibility = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')
    image1 = models.ImageField(upload_to='image/')
    image2 = models.ImageField(upload_to='image/', default="")
    timeStamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'PHOTO of  ' + self.roomtitle


class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    check_in = models.DateField(auto_now=False)
    check_out = models.DateField()

    booking_id = models.CharField(max_length=100, default="null")

    def __str__(self):
        return self.guest.username
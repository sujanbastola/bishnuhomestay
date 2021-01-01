from django.contrib import admin
from Rooms.models import room, Reservation

# Register your models here.
admin.site.register(room)
admin.site.register(Reservation)

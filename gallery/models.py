from django.db import models
from datetime import datetime


# Create your models here.
class imggal(models.Model):
    imgtitle=models.CharField(max_length=100)
    imgdesc = models.CharField(max_length=400)
    image = models.ImageField(upload_to='image/')
    timeStamp = models.DateTimeField(blank=True, null=True)

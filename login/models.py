from django.db import models

# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' _ ' + self.email


class carusel(models.Model):
    imgtitle =models.CharField(max_length=100)
    imgdesc = models.CharField(max_length=400)
    image = models.ImageField(upload_to='image/')


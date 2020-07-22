from django.db import models
from django.db.models.signals import pre_save
from ecomm.utils import unique_slug_generator


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    auther = models.CharField(max_length=100)
    slug = models.CharField(max_length=190, null=True, blank=True,unique=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.auther


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance )


pre_save.connect(slug_generator, sender=Post)

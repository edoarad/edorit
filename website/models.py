from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=1023)
    table_name = models.CharField(max_length=1023)
    photo = models.ImageField(upload_to = "img/guest_photos", default="img/guest_photos/default.jpg")


class Dancer(models.Model):

    video = models.FileField(upload_to='dancefloor', null=True)
    offset_top = models.FloatField(null=True)
    offset_left = models.FloatField(null=True)

    @property
    def ready(self):
        return self.offset_top is not None and self.offset_left is not None

class Greeting(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=32768)
    private = models.BooleanField()

from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=1023)
    table_name = models.CharField(max_length=1023)
    photo = models.ImageField(upload_to = "guest_photos", default="guest_photos/default.jpg")

class Greeting(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=32768)
    private = models.BooleanField()
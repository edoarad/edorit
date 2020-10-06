from django.db import models


# class Item(models.Model):
#     text = models.CharField(max_length=1023)


class Guest(models.Model):
    name = models.CharField(max_length=1023)
    table_name = models.CharField(max_length=1023)
    photo = models.ImageField(upload_to = "img/guest_photos", default="img/guest_photos/default.jpg")
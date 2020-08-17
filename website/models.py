from django.db import models


class Item(models.Model):
    text = models.CharField(max_length=1023)

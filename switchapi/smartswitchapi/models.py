from django.db import models
from django.utils import timezone
import datetime


class Switchapi(models.Model):
    name = models.CharField(max_length=50, default=None)
    switch0 = models.CharField(max_length=50, default=None)
    switch1 = models.CharField(max_length=50, default=None)
    switch2 = models.CharField(max_length=50, default=None)
    switch3 = models.CharField(max_length=50, default=None)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.name

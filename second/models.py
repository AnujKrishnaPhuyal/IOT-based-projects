from django.db import models
from pickle import TRUE
from tkinter import Widget
from datetime import datetime, time

from django.urls import clear_script_prefix

# Create your models here.
class data_model(models.Model):
    temp = models.CharField(max_length=20, null=True)
    pul = models.CharField(max_length=20, null=True)
    oxy = models.CharField(max_length=20, null=True)
    timee = models.DateTimeField(default=datetime.now)

   


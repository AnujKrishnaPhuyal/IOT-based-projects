from django.contrib import admin
from .models import data_model
# Register your models here.

@admin.register(data_model)
class data_admin(admin.ModelAdmin):
    list_display = ['temp', 'pul','oxy','timee']
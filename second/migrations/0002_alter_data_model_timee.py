# Generated by Django 4.0.4 on 2022-05-01 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_model',
            name='timee',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-19 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugueteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childmodel',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 14, 46, 33, 140934)),
        ),
        migrations.AlterField(
            model_name='workermodel',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 14, 46, 33, 140934)),
        ),
    ]

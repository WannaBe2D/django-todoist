# Generated by Django 3.2 on 2021-04-23 10:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pud_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 10, 55, 58, 716506, tzinfo=utc)),
        ),
    ]
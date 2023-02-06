# Generated by Django 4.1 on 2023-02-06 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_please check out the event date'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='event',
            name='Please check out the event date',
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gte', datetime.datetime(2023, 2, 6, 10, 8, 57, 534749))), name='Please check out the event date'),
        ),
    ]

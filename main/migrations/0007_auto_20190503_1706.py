# Generated by Django 2.1.5 on 2019-05-03 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190503_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscenario',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 17, 6, 44, 386299)),
        ),
    ]

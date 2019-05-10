# Generated by Django 2.1.5 on 2019-05-03 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190503_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singletest',
            name='operating_mode',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=4),
        ),
        migrations.AlterField(
            model_name='testscenario',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 17, 10, 5, 430646)),
        ),
    ]

# Generated by Django 4.2.10 on 2024-03-28 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0037_alter_transaction_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]

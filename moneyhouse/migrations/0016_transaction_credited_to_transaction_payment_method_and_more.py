# Generated by Django 4.2.10 on 2024-03-13 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0015_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Credited_To',
            field=models.TextField(default='Default Credited To'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Payment_Method',
            field=models.TextField(default='Default Payment Method'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Recipient_Details',
            field=models.TextField(default='Default Recipient Details'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Sender_Details',
            field=models.TextField(default='Default Sender Details'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Transaction_Number',
            field=models.TextField(default='Default Transaction Number'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Transaction_Type',
            field=models.TextField(default='Default Transaction Type'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.TextField(default='Default Money Received'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]

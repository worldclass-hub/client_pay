# Generated by Django 4.2.10 on 2024-04-04 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0043_mymodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='bank_account_name',
            new_name='bank_account_number',
        ),
    ]

# Generated by Django 4.2.10 on 2024-03-10 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0004_remove_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]

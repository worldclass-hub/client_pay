# Generated by Django 4.2.10 on 2024-03-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0020_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='Your Username', max_length=150, unique=True),
        ),
    ]

# Generated by Django 4.2.10 on 2024-03-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0022_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='username', max_length=150, unique=True),
        ),
    ]

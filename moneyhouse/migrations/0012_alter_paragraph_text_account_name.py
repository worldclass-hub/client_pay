# Generated by Django 4.2.10 on 2024-03-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0011_paragraph_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='text_Account_name',
            field=models.TextField(null=True),
        ),
    ]

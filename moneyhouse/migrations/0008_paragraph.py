# Generated by Django 4.2.10 on 2024-03-12 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moneyhouse', '0007_messagebox'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph_class', models.CharField(blank=True, default='default_paragraph_class', max_length=50)),
                ('text', models.TextField()),
                ('message_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='moneyhouse.messagebox')),
            ],
        ),
    ]

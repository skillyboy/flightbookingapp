# Generated by Django 5.0.2 on 2024-02-24 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='code',
        ),
        migrations.RemoveField(
            model_name='airport',
            name='timezone',
        ),
    ]

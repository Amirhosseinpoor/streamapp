# Generated by Django 5.1.2 on 2024-10-24 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chunking', '0003_remove_videomodels_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videomodels',
            name='title',
        ),
    ]
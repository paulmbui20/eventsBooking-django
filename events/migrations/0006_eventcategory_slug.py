# Generated by Django 5.1.2 on 2024-11-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

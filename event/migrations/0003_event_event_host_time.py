# Generated by Django 4.2.11 on 2024-03-06 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_options_event_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_host_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
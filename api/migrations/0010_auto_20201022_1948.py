# Generated by Django 3.0.5 on 2020-10-22 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201022_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titles',
            name='genre',
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre', to='api.Genres'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-10-12 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='score',
        ),
        migrations.AlterField(
            model_name='comments',
            name='reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='api.Review'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-10-25 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20201025_1714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('-year',), 'verbose_name': 'Title'},
        ),
    ]

# Generated by Django 3.0.5 on 2020-10-25 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20201025_1703'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('-name',), 'verbose_name': 'Genre'},
        ),
    ]

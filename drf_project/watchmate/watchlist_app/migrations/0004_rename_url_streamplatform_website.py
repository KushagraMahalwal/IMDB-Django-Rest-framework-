# Generated by Django 4.2.3 on 2023-12-15 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_watchlist_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='streamplatform',
            old_name='url',
            new_name='website',
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-28 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='vaxiat_isargari',
            new_name='vaziat_isargari',
        ),
    ]

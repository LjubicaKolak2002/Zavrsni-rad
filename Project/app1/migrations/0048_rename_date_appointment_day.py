# Generated by Django 4.0.5 on 2023-05-16 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0047_rename_day_appointment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='day',
        ),
    ]
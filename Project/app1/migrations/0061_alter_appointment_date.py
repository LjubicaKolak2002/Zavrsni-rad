# Generated by Django 4.0.5 on 2023-06-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0060_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
    ]

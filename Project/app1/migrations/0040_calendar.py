# Generated by Django 4.0.5 on 2023-05-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_delete_appointment2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
            ],
        ),
    ]
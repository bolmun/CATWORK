# Generated by Django 2.2.5 on 2020-05-24 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vet',
            name='care_taker',
        ),
    ]

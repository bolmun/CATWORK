# Generated by Django 2.2.5 on 2020-08-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200705_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='Please introduce yourself briefly'),
        ),
    ]
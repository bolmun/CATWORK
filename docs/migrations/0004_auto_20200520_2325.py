# Generated by Django 2.2.5 on 2020-05-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_auto_20200520_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='reason_adopt',
            field=models.TextField(),
        ),
    ]

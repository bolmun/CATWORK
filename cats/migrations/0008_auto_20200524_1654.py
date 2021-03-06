# Generated by Django 2.2.5 on 2020-05-24 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0007_auto_20200524_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appearance',
            options={'verbose_name_plural': 'Appearance'},
        ),
        migrations.AlterField(
            model_name='cat',
            name='appearance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='cats.Appearance'),
        ),
    ]

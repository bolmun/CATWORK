# Generated by Django 2.2.5 on 2020-05-20 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0002_auto_20200520_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doc',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='cats.Cat'),
        ),
        migrations.AddField(
            model_name='doc',
            name='housing_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='docs.HousingType'),
        ),
    ]

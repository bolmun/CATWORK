# Generated by Django 2.2.5 on 2020-05-24 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0006_auto_20200521_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Diagnosis',
            },
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('visit_date', models.DateField()),
                ('vet_title', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('is_vaccination', models.BooleanField()),
                ('vaccination', models.CharField(blank=True, max_length=100, null=True)),
                ('prescription', models.TextField(blank=True)),
                ('expense', models.IntegerField(blank=True, null=True)),
                ('reciept', models.FileField(blank=True, null=True, upload_to='')),
                ('care_taker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vets', to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vets', to='cats.Cat')),
                ('diagnosis', models.ManyToManyField(blank=True, related_name='vets', to='vets.Diagnosis')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

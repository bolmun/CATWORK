# Generated by Django 2.2.5 on 2020-05-20 04:12

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('is_rented', models.BooleanField(default=False)),
                ('landlord_agree', models.BooleanField(default=True)),
                ('job', models.CharField(max_length=100)),
                ('company_title', models.CharField(blank=True, max_length=100, null=True)),
                ('id_card', models.ImageField(upload_to='')),
                ('job_certification', models.ImageField(blank=True, null=True, upload_to='')),
                ('instagram_id', models.CharField(blank=True, max_length=50, null=True)),
                ('married', models.BooleanField(default=False)),
                ('family_num', models.IntegerField()),
                ('children_num', models.IntegerField()),
                ('current_cat', models.IntegerField()),
                ('first_ever_cat', models.BooleanField(default=False)),
                ('other_companion_animals', models.IntegerField()),
                ('budget_plan', models.IntegerField()),
                ('insurance_plan', models.BooleanField(default=True)),
                ('protect_window', models.BooleanField(default=True)),
                ('protect_door', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HousingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'House Types',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='home_photos')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_doc', to='docs.Doc')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

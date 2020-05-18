# Generated by Django 2.2.5 on 2020-05-18 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=80)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('is_neutered', models.BooleanField(default=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('skittishness', models.IntegerField()),
                ('outgoingness', models.IntegerField()),
                ('dominance', models.IntegerField()),
                ('spontaneity', models.IntegerField()),
                ('friendliness', models.IntegerField()),
                ('rescue_story', models.TextField()),
                ('barcode', models.IntegerField(blank=True, null=True)),
                ('adopted', models.BooleanField(default=False)),
                ('bro_sis', models.ManyToManyField(blank=True, null=True, related_name='cats_bs', to='cats.Cat')),
            ],
            options={
                'abstract': False,
            },
        ),
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
            name='HealthCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Health Issues',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='cat_photos')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='cats.Cat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
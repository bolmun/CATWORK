# Generated by Django 2.2.5 on 2020-05-20 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', '입양 계약서 내용 확인 중'), ('confirmed', '입양 계약 확정'), ('canceled', '입양 계약 취소')], max_length=30)),
                ('contents', models.TextField()),
                ('agreed_applicant', models.BooleanField(default=False)),
                ('agreed_care_taker', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

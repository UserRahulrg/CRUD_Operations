# Generated by Django 4.1.7 on 2023-03-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('name', models.CharField(max_length=80)),
                ('course', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=80)),
                ('rollno', models.IntegerField()),
                ('batch', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alaqe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60000)),
                ('phone_number', models.CharField(max_length=5000)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Qeyd edilmiş Əlaqə',
                'verbose_name_plural': 'Qeyd edilmiş Əlaqə',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.CharField(max_length=4000)),
            ],
            options={
                'verbose_name': 'Xəritə',
                'verbose_name_plural': 'Xəritə',
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xaber', '0002_alter_xaber_name_alter_xaber_name_az_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xaber',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
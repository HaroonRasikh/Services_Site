# Generated by Django 4.1.7 on 2023-06-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('komite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komite',
            name='menue_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='komite',
            name='menue_name_az',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='komite',
            name='menue_name_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='komite',
            name='menue_name_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='komite_1',
            name='menue_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='komite_1',
            name='menue_name_az',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='komite_1',
            name='menue_name_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='komite_1',
            name='menue_name_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='title'),
        ),
    ]

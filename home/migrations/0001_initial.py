# Generated by Django 4.1.7 on 2023-06-02 19:13

import ckeditor.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('name_az', models.CharField(blank=True, max_length=2000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=2000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=2000, null=True)),
                ('logo', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Loqolar',
                'verbose_name_plural': 'Loqolar',
            },
        ),
        migrations.CreateModel(
            name='MainPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='images/')),
                ('image_2', models.ImageField(upload_to='images/')),
                ('image_3', models.ImageField(upload_to='images/')),
                ('title', models.TextField()),
                ('title_az', models.TextField(null=True)),
                ('title_en', models.TextField(null=True)),
                ('title_ru', models.TextField(null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_az', ckeditor.fields.RichTextField(null=True)),
                ('description_en', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
            ],
            options={
                'verbose_name': 'əsas səhifə slide',
                'verbose_name_plural': 'əsas səhifə slide',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3000)),
                ('name_az', models.CharField(max_length=3000, null=True)),
                ('name_en', models.CharField(max_length=3000, null=True)),
                ('name_ru', models.CharField(max_length=3000, null=True)),
                ('title', models.TextField()),
                ('title_az', models.TextField(null=True)),
                ('title_en', models.TextField(null=True)),
                ('title_ru', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('description', tinymce.models.HTMLField()),
                ('description_az', tinymce.models.HTMLField(null=True)),
                ('description_en', tinymce.models.HTMLField(null=True)),
                ('description_ru', tinymce.models.HTMLField(null=True)),
            ],
            options={
                'verbose_name': 'xəbərlər',
                'verbose_name_plural': 'xəbərlər',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(max_length=3000)),
                ('description_az', models.CharField(max_length=3000, null=True)),
                ('description_en', models.CharField(max_length=3000, null=True)),
                ('description_ru', models.CharField(max_length=3000, null=True)),
            ],
            options={
                'verbose_name': 'Əsas səhifə servislər',
                'verbose_name_plural': 'Əsas səhifə servislər',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3000)),
                ('name_az', models.CharField(max_length=3000, null=True)),
                ('name_en', models.CharField(max_length=3000, null=True)),
                ('name_ru', models.CharField(max_length=3000, null=True)),
                ('date', models.CharField(max_length=3000)),
                ('date_az', models.CharField(max_length=3000, null=True)),
                ('date_en', models.CharField(max_length=3000, null=True)),
                ('date_ru', models.CharField(max_length=3000, null=True)),
                ('title', models.CharField(max_length=3000)),
                ('title_az', models.CharField(max_length=3000, null=True)),
                ('title_en', models.CharField(max_length=3000, null=True)),
                ('title_ru', models.CharField(max_length=3000, null=True)),
                ('description', models.TextField()),
                ('description_az', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Tarixlər',
                'verbose_name_plural': 'Tarixlər',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('name_az', models.CharField(blank=True, max_length=2000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=2000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', tinymce.models.HTMLField()),
                ('description_az', tinymce.models.HTMLField(null=True)),
                ('description_en', tinymce.models.HTMLField(null=True)),
                ('description_ru', tinymce.models.HTMLField(null=True)),
            ],
            options={
                'verbose_name': 'Sponsorlar',
                'verbose_name_plural': 'Sponsorlar',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('title_az', models.CharField(max_length=2000, null=True)),
                ('title_en', models.CharField(max_length=2000, null=True)),
                ('title_ru', models.CharField(max_length=2000, null=True)),
                ('description', tinymce.models.HTMLField()),
                ('description_az', tinymce.models.HTMLField(null=True)),
                ('description_en', tinymce.models.HTMLField(null=True)),
                ('description_ru', tinymce.models.HTMLField(null=True)),
            ],
            options={
                'verbose_name': 'Əsas səhifə Dəvət',
                'verbose_name_plural': 'Əsas səhifə Dəvət',
            },
        ),
        migrations.CreateModel(
            name='TimeDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
            ],
            options={
                'verbose_name': 'geri sayım taymeri',
                'verbose_name_plural': 'geri sayım taymeri',
            },
        ),
        migrations.CreateModel(
            name='UpcomingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=2000)),
                ('date_az', models.CharField(max_length=2000, null=True)),
                ('date_en', models.CharField(max_length=2000, null=True)),
                ('date_ru', models.CharField(max_length=2000, null=True)),
                ('statement', models.TextField()),
                ('statement_az', models.TextField(null=True)),
                ('statement_en', models.TextField(null=True)),
                ('statement_ru', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Göy Yaşıl Dördkünc',
                'verbose_name_plural': 'Göy Yaşıl Dördkünc',
            },
        ),
    ]

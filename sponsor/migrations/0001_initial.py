# Generated by Django 4.1.7 on 2023-06-02 19:13

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category1',
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
                'verbose_name': 'Kateqoriya 2',
                'verbose_name_plural': 'Kateqoriya 2',
            },
        ),
        migrations.CreateModel(
            name='category2',
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
                'verbose_name': 'Kateqoriya 3',
                'verbose_name_plural': 'Kateqoriya 3',
            },
        ),
        migrations.CreateModel(
            name='category3',
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
                'verbose_name': 'Kateqoriya 4',
                'verbose_name_plural': 'Kateqoriya 4',
            },
        ),
        migrations.CreateModel(
            name='category4',
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
                'verbose_name': 'Kateqoriya 5',
                'verbose_name_plural': 'Kateqoriya 5',
            },
        ),
        migrations.CreateModel(
            name='mainSponsor',
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
                'verbose_name': 'Kateqoriya 1',
                'verbose_name_plural': 'Kateqoriya 1',
            },
        ),
        migrations.CreateModel(
            name='Sponsorsave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('surname', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=2000)),
                ('mobile', models.CharField(max_length=2000)),
                ('company_name', models.CharField(max_length=2000)),
                ('conference_name', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Qeyd edilmiş Sponsorlar',
                'verbose_name_plural': 'Qeyd edilmiş Sponsorlar',
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_gallery_date_alter_gallery_date_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='date_detail',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]

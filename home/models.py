from django.db import models
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models

# Create your models here.


class MainPhoto(models.Model):
    image_1 = models.ImageField(upload_to="images/")
    image_2 = models.ImageField(null=True, blank=True,upload_to="images/")
    image_3 = models.ImageField(null=True, blank=True,upload_to="images/")
    
    title = models.TextField()
    #description = tinymce_models.HTMLField()
    description = RichTextField()
    class Meta:
        verbose_name = 'əsas səhifə slide'
        verbose_name_plural = 'əsas səhifə slide'

class Photo(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.CharField(max_length=3000)
    class Meta:
        verbose_name = 'Əsas səhifə servislər'
        verbose_name_plural = 'Əsas səhifə servislər'

class Subject(models.Model):
    title = models.CharField(max_length=2000)
    description = tinymce_models.HTMLField()
    class Meta:
        verbose_name = 'Əsas səhifə Dəvət'
        verbose_name_plural = 'Əsas səhifə Dəvət'

class Schedule(models.Model):
    name = models.CharField(null=True, blank=True,max_length=3000)
    date = models.CharField(max_length=3000)
    title = models.CharField(max_length=3000)
    description = models.TextField()
    class Meta:
        verbose_name = 'Tarixlər'
        verbose_name_plural = 'Tarixlər'

 

class TimeDown(models.Model):
    date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    class Meta:
        verbose_name = 'geri sayım taymeri'
        verbose_name_plural = 'geri sayım taymeri'

class News(models.Model):
    name = models.CharField(blank=True,null=True,max_length=3000)
    title = models.TextField()
    image = models.ImageField(upload_to="images")
    description = tinymce_models.HTMLField()

    class Meta:
        verbose_name = 'xəbərlər'
        verbose_name_plural = 'xəbərlər'
    
    

   

class UpcomingEvent(models.Model):
    date = models.CharField(max_length=2000)
    statement= models.TextField()

    class Meta:
        verbose_name = 'Göy Yaşıl Dördkünc'
        verbose_name_plural = 'Göy Yaşıl Dördkünc'



 


class Sponsor(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    description =tinymce_models.HTMLField()
    class Meta:
        verbose_name = 'Sponsorlar'
        verbose_name_plural = 'Sponsorlar'


class Logo(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    logo = models.ImageField(upload_to="images/")
    class Meta:
        verbose_name = 'Loqolar'
        verbose_name_plural = 'Loqolar'

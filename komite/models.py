from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Komite(models.Model):
    menue_name = models.CharField('title',blank=True,null=True,max_length=1000) 
    name = models.CharField(max_length= 2000)
    profile = models.ImageField(upload_to="images/")
    about = models.TextField()
    social1 = models.CharField(max_length=1000)
    social2 = models.CharField(max_length=1000)
    social3 = models.CharField(max_length=1000)
    class Meta:
        verbose_name='Komitə 1'
        verbose_name_plural='Komitə 1'





class Komite_1(models.Model):
    menue_name = models.CharField('title',blank=True,null=True,max_length=1000) 
    name = models.CharField(max_length= 2000)
    profile = models.ImageField(upload_to="images/")
    about = models.TextField()
    social1 = models.CharField(max_length=1000)
    social2 = models.CharField(max_length=1000)
    social3 = models.CharField(max_length=1000)
 
    
    class Meta:
        verbose_name='Komitə 2'
        verbose_name_plural='Komitə 2'
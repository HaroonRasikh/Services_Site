from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Program(models.Model):
    name = models.CharField(null=True,blank=True,max_length=1000)
    title = models.CharField(null=True,blank=True,max_length=2000)
    description = RichTextField()
    file = models.FileField(upload_to='images/',null=True,blank=True)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural='Program'

 
class Event(models.Model):
    title = models.CharField(null=True,blank=True,max_length=1000)
    time  = models.CharField(max_length=2000)
    description = RichTextField()
    class Meta:
        verbose_name = 'Program Tarixləri'
        verbose_name_plural='Program Tarixləri'



class Manager(models.Model):
    image= models.ImageField(upload_to="images/")
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = 'Rektorlar'
        verbose_name_plural='Rektorlar'


class Event_2(models.Model):
    title = models.CharField(null=True,blank=True,max_length=1000)
    time  = models.CharField(max_length=2000)
    description = RichTextField()

    class Meta:
        verbose_name = 'Program Sxema '
        verbose_name_plural='Program Sxema '

from django.db import models

# Create your models here.

class Gallery(models.Model):
    title_name = models.CharField(null=True,blank=True,max_length=1000)
    title = models.TextField()
    date = models.DateField(auto_now_add=False, auto_now=False,blank=True,null=True)
    date_detail =models.CharField(null=True,blank=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    class Meta:
        verbose_name='Şəkillər'
        verbose_name_plural='Şəkillər'



class Video(models.Model):
    video = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=False, auto_now=False,blank=True,null=True)
    date_detail =models.CharField(max_length=2000,blank=True, null=True)


    class Meta:
        verbose_name='Videolar'
        verbose_name_plural='Videolar'
    
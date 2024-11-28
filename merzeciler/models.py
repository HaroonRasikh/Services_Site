from django.db import models

# Create your models here.

class Maruzacilar(models.Model):
    menue_name = models.CharField(blank=True,null=True,max_length=1000) 
    name = models.CharField(max_length= 2000)
    profile = models.ImageField(upload_to="images/")
    about = models.TextField()
    social1 = models.CharField(max_length=1000)
    social2 = models.CharField(max_length=1000)
    social3 = models.CharField(max_length=1000)

 
    class Meta:
        verbose_name='Məruzəçilər 1'
        verbose_name_plural='Məruzəçilər 1'

    
class Maruzacilar_1(models.Model):
    menue_name = models.CharField(blank=True,null=True,max_length=1000) 
    name = models.CharField(max_length= 2000)
    profile = models.ImageField(upload_to="images/")
    about = models.TextField()
    social1 = models.CharField(max_length=1000)
    social2 = models.CharField(max_length=1000)
    social3 = models.CharField(max_length=1000)
 
    
    class Meta:
        verbose_name='Məruzəçilər 2'
        verbose_name_plural='Məruzəçilər 2'


    
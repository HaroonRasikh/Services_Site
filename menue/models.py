from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Menue(models.Model):
    image = models.ImageField(verbose_name='header_logo', upload_to="images/")
    menue_1 = models.CharField(max_length=2000)
    menue_2 = models.CharField(max_length=2000)
    menue_3 = models.CharField(max_length=2000)
    menue_4 = models.CharField(max_length=2000)
    menue_5 = models.CharField(max_length=2000)
    menue_6 = models.CharField(max_length=2000)
    menue_7 = models.CharField(max_length=2000)
    menue_8 = models.CharField(max_length=2000,default=None)
    menue_9 = models.CharField(max_length=2000)
    menue_10 = models.CharField(max_length=2000)
    menue_11 = models.CharField(max_length=2000)
    menue_12 = models.CharField(max_length=2000)
    menue_13 = models.CharField(max_length=2000)
    menue_14 = models.CharField(max_length=2000)
    menue_15 = models.CharField(max_length=2000)
    menue_16 = models.CharField(max_length=2000)
    menue_17 = models.CharField(max_length=2000)
    menue_18 = models.CharField(max_length=2000)
    menue_19 = models.CharField(max_length=2000)
    menue_20 = models.CharField(max_length=2000)

    slug = models.TextField(max_length=70000)  
    image2 = models.ImageField(verbose_name = 'footer_logo', upload_to="images/")

    class Meta:
        verbose_name = 'Menyular'
        verbose_name_plural='Menyular'

class Number(models.Model):
    number = PhoneNumberField()
    class Meta:
        verbose_name = 'Nömrələr'
        verbose_name_plural='Nömrələr'    

class Email(models.Model):
    email = models.EmailField()
    class Meta:
        verbose_name = 'E-poçtlar'
        verbose_name_plural='E-poçtlar'
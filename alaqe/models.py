from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Map(models.Model):
    map = models.CharField(max_length=4000)

    class Meta:
        verbose_name='Xəritə'
        verbose_name_plural='Xəritə'
class Alaqe(models.Model):
    name = models.CharField(max_length=60000)
    phone_number = models.CharField(max_length=5000)
    message = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Qeyd edilmiş Əlaqə'
        verbose_name_plural='Qeyd edilmiş Əlaqə'

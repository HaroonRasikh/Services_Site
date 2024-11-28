from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class mainSponsor(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    description =tinymce_models.HTMLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kateqoriya 1'
        verbose_name_plural='Kateqoriya 1'

class category1(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    description =tinymce_models.HTMLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kateqoriya 2'
        verbose_name_plural='Kateqoriya 2'
    
class category2(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    description =tinymce_models.HTMLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kateqoriya 3'
        verbose_name_plural='Kateqoriya 3'
    
class category3(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    description =tinymce_models.HTMLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kateqoriya 4'
        verbose_name_plural='Kateqoriya 4'

class category4(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    description =tinymce_models.HTMLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kateqoriya 5'
        verbose_name_plural='Kateqoriya 5'
class Sponsorsave(models.Model):
    name = models.CharField(max_length=1000)
    surname = models.CharField(max_length=1000)
    email = models.CharField(max_length=2000)
    mobile = models.CharField(max_length=2000)
    company_name= models.CharField(max_length=2000)
    conference_name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Qeyd edilmiş Sponsorlar'
        verbose_name_plural='Qeyd edilmiş Sponsorlar'
    

    
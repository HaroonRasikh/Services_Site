from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class About(models.Model):
    name = models.CharField(blank=True,null=True,max_length=2000)
    image = models.ImageField(upload_to="images/")
    main_description = tinymce_models.HTMLField()
    sub_description1 = tinymce_models.HTMLField()
    sub_description2 = tinymce_models.HTMLField()
    sub_description3 = tinymce_models.HTMLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Haqqımda'
        verbose_name_plural = 'Haqqımda'
    
class People(models.Model):
    name = models.CharField(max_length=3000)
    profile = models.ImageField(upload_to="images/")
    about = models.TextField()

    class Meta:
        verbose_name = 'Şəxslər'
        verbose_name_plural='Şəxslər'
    
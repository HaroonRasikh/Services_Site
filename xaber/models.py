from django.db import models
from tinymce import models as tinymce_models
# Create your models here.

class Xaber(models.Model):
    name = models.CharField(null=True,blank=True,max_length=3000)
    title = models.TextField()
    image = models.ImageField(upload_to="images/")
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True,null=True)
    description = tinymce_models.HTMLField()

    class Meta:
        verbose_name = 'XƏBƏRLƏR'
        verbose_name_plural = 'XƏBƏRLƏR'
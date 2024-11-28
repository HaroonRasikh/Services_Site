from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Abstract_0(models.Model):
    title = models.CharField(max_length=20000)
    description=RichTextField()
    class Meta:
        verbose_name = 'Onlayn Abstrakt Təqdimatı'
        verbose_name_plural='Onlayn Abstrakt Təqdimatı'


class Abstract_1(models.Model):
    title_name = models.CharField(null=True,blank=True,max_length=20000)
    title = models.CharField(max_length=20000)
    description=RichTextField()
    class Meta:
        verbose_name = 'Abstrakt Təlimatları'
        verbose_name_plural='Abstrakt Təlimatları'

class Abstract_2(models.Model):
    title_name = models.CharField(null=True,blank=True,max_length=20000)
    title = models.CharField(max_length=20000)
    description=RichTextField()
    class Meta:
        verbose_name = 'Abstrakt Təqdimat Təlimatı'
        verbose_name_plural='Abstrakt Təqdimat Təlimatı'

class Abstract_3(models.Model):
    title_name = models.CharField(null=True,blank=True,max_length=20000)
    title = models.CharField(max_length=20000)
    description=RichTextField()
    class Meta:
        verbose_name = 'Abstrakt seçimi'
        verbose_name_plural='Abstrakt seçimi'

class Abstract_4(models.Model):
    title_name = models.CharField(null=True,blank=True,max_length=20000)
    title = models.CharField(max_length=20000)
    description=RichTextField()
    class Meta:
        verbose_name = 'Abstrakt Kateqoriyalar'
        verbose_name_plural='Abstrakt Kateqoriyalar'

class Abstract_5(models.Model):
    title_name = models.CharField(null=True,blank=True,max_length=20000)
    title = models.CharField(max_length=20000)
    description=RichTextField()
    class Meta:
        verbose_name = 'Mükafat Qrantları'
        verbose_name_plural='Mükafat Qrantları'




class Abstract_Number(models.Model):
    number = PhoneNumberField()
    class Meta:
        verbose_name = 'Nömrə'
        verbose_name_plural='Nömrə'


class Abstract_Email(models.Model):
    email = models.EmailField()
    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural='E-mail'

class Text(models.Model):
    description = models.TextField()
    class Meta:
        verbose_name = 'mətn'
        verbose_name_plural='mətn'


class FormInformation(models.Model):
    form_title = models.TextField()
    title_1 = models.CharField(max_length=5000)
    option =models.CharField(max_length=5000)
    option_1 = models.CharField(max_length=5000)
    option_2 = models.CharField(max_length=5000)
    option_3 = models.CharField(max_length=5000)
    option_4 = models.CharField(max_length=5000)
    option_1 = models.CharField(max_length=5000)
    


#-----------------------------Anket Modelleri------------------------------
#--------------------------------------------------------------------------



class dropdown1options(models.Model):
    option = models.CharField(max_length=1000)
    def __str__(self):
        return self.option
    class Meta:
        verbose_name = 'dropdown 1'
        verbose_name_plural='dropdown 1'

class dropdown2options(models.Model):
    option = models.CharField(max_length=1000)
    def __str__(self):
        return self.option
    class Meta:
        verbose_name = 'dropdown 2'
        verbose_name_plural='dropdown 2'
class dropdown3options(models.Model):
    option = models.CharField(max_length=1000)
    def __str__(self):
        return self.option
    class Meta:
        verbose_name = 'dropdown 3'
        verbose_name_plural='dropdown 3'

class dropdown4options(models.Model):
    option = models.CharField(max_length=1000)
    def __str__(self):
        return self.option
    class Meta:
        verbose_name = 'dropdown 4'
        verbose_name_plural='dropdown 4'
class dropdown5options(models.Model):
    option = models.CharField(max_length=200)
    def __str__(self):
        return self.option
    class Meta:
        verbose_name = 'dropdown 5'
        verbose_name_plural='dropdown 5'
class selectbox1options(models.Model):
    option = models.CharField(max_length=1000)
    def __str__(self):
        return self.option
    class Meta:
        verbose_name = 'dropdown 6'
        verbose_name_plural='dropdown 6'
class selectbox2options(models.Model):
    option = models.CharField(max_length=1000)
    def __str__(self):
        return self.option
    class Meta:
        verbose_name = 'dropdown 7'
        verbose_name_plural='dropdown 7'

class Survey(models.Model):
    textbox1 = models.CharField(verbose_name='textbox 1',max_length=20000)
    dropdown_1 = models.ForeignKey(dropdown1options,on_delete=models.CASCADE)
    dropdown_2 = models.ForeignKey(dropdown2options, on_delete=models.CASCADE)
    dropdown_3 = models.ForeignKey(dropdown3options,on_delete=models.CASCADE)
    dropdown_4 = models.ForeignKey(dropdown4options,on_delete=models.CASCADE)
    select1 = models.BooleanField(verbose_name='select 1',default=False, null=True, blank=True)
    textbox2 = models.CharField(verbose_name='textbox 2',max_length=20000)
    select2 = models.BooleanField(verbose_name='select 2',default=False, null=True, blank=True)


    dropdown_5 = models.ForeignKey(dropdown5options,on_delete=models.CASCADE)
    lastname = models.CharField(max_length=500)
    name = models.CharField(verbose_name='first name',max_length=255)
    email = models.EmailField()
    first_name_init = models.CharField(verbose_name='first name init',max_length=500)
    affilation = models.CharField(max_length=500)
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=500)


    background = models.TextField()
    method = models.TextField()
    result = models.TextField()
    conclusion = models.TextField()
    file_1 = models.FileField(verbose_name = 'fiel 1', upload_to="images/")
    file_2 = models.FileField(verbose_name = 'fiel 2', upload_to="images/")
    file_3 = models.FileField(verbose_name = 'fiel 3', upload_to="images/")
    selectbox_1 = models.ForeignKey(selectbox1options,on_delete=models.CASCADE)
    selectbox_2 = models.ForeignKey(selectbox2options,on_delete=models.CASCADE)
    keyword_1 = models.CharField(verbose_name='keyword 1',max_length=2000) 
    checkbox_1 = models.BooleanField(verbose_name='checkbox 1',default=False, null=True, blank=True)
    checkbox_2 = models.BooleanField(verbose_name='checkbox 2',default=False, null=True, blank=True)
    checkbox_3 = models.BooleanField(verbose_name='checkbox 3',default=False, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Anket'
        verbose_name_plural='Anket'

class RowSubmission(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    dropdown_5 = models.ForeignKey(dropdown5options,on_delete=models.CASCADE)
    lastname = models.CharField(max_length=500)
    name = models.CharField(verbose_name='first name',max_length=255)
    email = models.EmailField()
    first_name_init = models.CharField(verbose_name='first name init',max_length=500)
    affilation = models.CharField(max_length=500)
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=500)
    email2= models.CharField(max_length=1000)
   
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Yeni Şəxsiyyət (anket)'
        verbose_name_plural='Yeni Şəxsiyyət (anket)'

   

class Draft(models.Model):
    textbox1 = models.CharField(verbose_name='textbox 1',max_length=20000)
    dropdown_1 = models.ForeignKey(dropdown1options,on_delete=models.CASCADE)
    dropdown_2 = models.ForeignKey(dropdown2options, on_delete=models.CASCADE)
    dropdown_3 = models.ForeignKey(dropdown3options,on_delete=models.CASCADE)
    dropdown_4 = models.ForeignKey(dropdown4options,on_delete=models.CASCADE)
    select1 = models.BooleanField(verbose_name='select 1',default=False, null=True, blank=True)
    textbox2 = models.CharField(verbose_name='textbox 2',max_length=20000)
    select2 = models.BooleanField(verbose_name='select 2',default=False, null=True, blank=True)

    dropdown_5 = models.ForeignKey(dropdown5options,on_delete=models.CASCADE)
    lastname = models.CharField(max_length=500)
    name = models.CharField(verbose_name='first name',max_length=255)
    email = models.EmailField()
    first_name_init = models.CharField(verbose_name='first name init',max_length=500)
    affilation = models.CharField(max_length=500)
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=500)

    background = models.TextField()
    method = models.TextField()
    result = models.TextField()
    conclusion = models.TextField()
    file_1 = models.FileField(verbose_name = 'fiel 1', upload_to="images/")
    file_2 = models.FileField(verbose_name = 'fiel 2', upload_to="images/")
    file_3 = models.FileField(verbose_name = 'fiel 3', upload_to="images/")
    selectbox_1 = models.ForeignKey(selectbox1options,on_delete=models.CASCADE)
    selectbox_2 = models.ForeignKey(selectbox2options,on_delete=models.CASCADE)
    keyword_1 = models.CharField(verbose_name='keyword 1',max_length=2000) 
    checkbox_1 = models.BooleanField(verbose_name='checkbox_1',default=False, null=True, blank=True)
    checkbox_2 = models.BooleanField(verbose_name='checkbox_2',default=False, null=True, blank=True)
    checkbox_3 = models.BooleanField(verbose_name='checkbox_3',default=False, null=True, blank=True)
    email2= models.CharField(max_length=1000)

   
    def __str__(self):
        return self.name
    



class DraftRow_Submission(models.Model):
    survey = models.ForeignKey(Draft,on_delete=models.CASCADE)
    dropdown_5 = models.ForeignKey(dropdown5options,on_delete=models.CASCADE)
    lastname = models.CharField(max_length=500)
    name = models.CharField(verbose_name='first name',max_length=255)
    email = models.EmailField()
    first_name_init = models.CharField(verbose_name='first name init',max_length=500)
    affilation = models.CharField(max_length=500)
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=500)
    

    def __str__(self):
        return self.name




class SurveyTitle(models.Model):
    maintitle = models.CharField(max_length=20000)
    input1 = models.CharField(max_length=2000)
    dropdown1=models.CharField(max_length=2000)
    dropdown2=models.CharField(max_length=2000)
    dropdown3=models.CharField(max_length=2000)
    dropdown4=models.CharField(max_length=2000)
    checkboxtitle1= models.CharField(max_length=2000)
    checkbox1=models.CharField(max_length=2000)
    input2 = models.CharField(max_length=2000)
    checkboxtitle2= models.CharField(max_length=2000)
    checkbox2=models.CharField(max_length=2000)
    presentertitle=models.CharField(max_length=20000)
    presnterdropdown=models.CharField(max_length=2000)
    lastnametitle = models.CharField(max_length=2000)
    firstnametitle = models.CharField(max_length=2000)
    emailtitle = models.CharField(max_length=2000)
    firstnameInititle= models.CharField(max_length=2000)
    affiliationtitle = models.CharField(max_length=2000)
    citytitle = models.CharField(max_length=2000)
    countrytitle = models.CharField(max_length=2000)
    buttontitle = models.CharField(max_length=2000)

    textinput1 = models.CharField(max_length=20000)
    textinput2 = models.CharField(max_length=20000)
    textinput3 = models.CharField(max_length=20000)
    textinput4 = models.CharField(max_length=20000)

    file1 = models.CharField(max_length=2000)
    file2 = models.CharField(max_length=2000)
    file3 = models.CharField(max_length=2000)
    selectdropdown1=models.CharField(max_length=2000)
    selectdropdown2=models.CharField(max_length=2000)
    keywordinput=models.CharField(max_length=2000)
    lastcheckboxtitle1= models.CharField(max_length=2000)
    lastcheckboxtitle2= models.CharField(max_length=2000)
    lastcheckboxtitle3= models.CharField(max_length=2000)
    
    def __str__(self):
        return self.maintitle
    class Meta:
        verbose_name = 'Anket başlıqları'
        verbose_name_plural='Anket başlıqları'

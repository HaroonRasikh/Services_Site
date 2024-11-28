# from about.models import About
from django import forms
 
# class SearchForm(forms.ModelForm):
# 	class Meta:
# 		model = About
# 		fields = ['name' ]

#from phonenumber_field.formfields import PhoneNumberField
class contactusForm(forms.Form):
    Name = forms.CharField(max_length=25,required=True)
    Mobile_number = forms.IntegerField(required=True)
    #subject = forms.CharField(required=True)
    Message = forms.CharField(widget=forms.Textarea,required=True)

class sponsorform(forms.Form):
    Name = forms.CharField(max_length=25,required=True)
    Surname = forms.CharField(max_length=25,required=True)
    Emailform = forms.CharField(max_length=25,required=True)
    Mobile = forms.IntegerField(required=True)
    Company = forms.CharField(max_length=25,required=True)
    Conference = forms.CharField(max_length=25,required=True)
   
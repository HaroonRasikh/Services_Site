
from modeltranslation.translator import TranslationOptions,register
from .models import *


@register(mainSponsor)
class sponsorTranslationOptions(TranslationOptions):
    fields = ('name','description',)

@register(category1)
class sponsorTranslationOptions(TranslationOptions):
    fields = ('name','description',)
 


@register(category2)
class sponsorTranslationOptions(TranslationOptions):
    fields = ('name','description',)
 
 
@register(category3)
class sponsorTranslationOptions(TranslationOptions):
    fields = ('name','description',)
 
 
@register(category4)
class sponsorTranslationOptions(TranslationOptions):
    fields = ('name','description',)
 

  







 

 



 



 






 
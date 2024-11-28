
from modeltranslation.translator import TranslationOptions,register
from .models import Komite,Komite_1
@register(Komite)
class KomiteTranslate(TranslationOptions):
    fields = ('menue_name', 'name' , 'about',)

@register(Komite_1)
class Komite1Translate(TranslationOptions):
    fields = ('menue_name', 'name' , 'about',)
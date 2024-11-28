from modeltranslation.translator import TranslationOptions,register
from .models import Maruzacilar,Maruzacilar_1
@register(Maruzacilar)
class merzeciTranslate(TranslationOptions):
    fields = ('menue_name', 'name' , 'about',)

@register(Maruzacilar_1)
class merzeciTranslate(TranslationOptions):
    fields = ('menue_name', 'name' , 'about',)
 
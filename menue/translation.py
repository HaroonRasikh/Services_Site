from modeltranslation.translator import TranslationOptions,register
from .models import Menue
@register(Menue)
class MenueTranslate(TranslationOptions):
    fields = ('menue_1','menue_2','menue_3','menue_4','menue_5','menue_6',
              'menue_7','menue_8','menue_9','menue_10','menue_11','menue_12',
              'menue_13','menue_14','menue_15','menue_16','menue_17','menue_18',
              'menue_19','menue_20','slug',)
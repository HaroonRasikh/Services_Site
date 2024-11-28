from modeltranslation.translator import TranslationOptions,register
from .models import Xaber
@register(Xaber)
class xaberTranslate(TranslationOptions):
    fields = ('name','title','description',)
from modeltranslation.translator import TranslationOptions,register
from .models import About,People
@register(About)
class AboutTranslate(TranslationOptions):
    fields = ('name','main_description','sub_description1','sub_description2','sub_description3',)

@register(People)
class AboutTranslate(TranslationOptions):
    fields = ('name','about',)
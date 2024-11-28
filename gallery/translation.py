from modeltranslation.translator import TranslationOptions,register
from .models import Gallery
@register(Gallery)
class GalleryTranslate(TranslationOptions):
    fields = ('title_name', 'title' ,'date_detail', 'description',)
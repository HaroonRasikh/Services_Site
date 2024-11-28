
from modeltranslation.translator import TranslationOptions,register
from .models import *

@register(MainPhoto)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title','description',)

@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Subject)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title','description',)

@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ('name','date','title','description',)
   

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name','title','description',)

@register(UpcomingEvent)
class upcomeeventTranslationOptions(TranslationOptions):
    fields = ('date','statement',)

@register(Sponsor)
class sponsorTranslationOptions(TranslationOptions):
    fields = ('name','description',)

@register(Logo)
class LogoTranslationOptions(TranslationOptions):
    fields = ('name',)


  







 

 



 



 






 
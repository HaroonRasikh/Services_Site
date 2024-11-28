
from modeltranslation.translator import TranslationOptions,register
from .models import *

@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('name','title','description')

@register(Event)
class EventTranslation(TranslationOptions):
    fields = ('title','description')
 
@register(Event_2)
class EventTranslation(TranslationOptions):
    fields = ('title','description')

@register(Manager)
class ManagerTranslation(TranslationOptions):
    fields = ('name','description')
 








 

 



 



 






 
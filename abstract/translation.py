
from modeltranslation.translator import TranslationOptions,register
from .models import *

@register(SurveyTitle)
class title(TranslationOptions):
    fields=('maintitle',
'input1',
'dropdown1',
'dropdown2',
'dropdown3',
'dropdown4',
'checkboxtitle1',
'checkbox1',
'input2',
'checkboxtitle2',
'checkbox2',
'presentertitle',
'presnterdropdown',
'lastnametitle',
'firstnametitle',
'emailtitle',
'firstnameInititle',
'affiliationtitle',
'citytitle',
'countrytitle',
'buttontitle',
'textinput1',
'textinput2',
'textinput3',
'textinput4',
'file1',
'file2',
'file3',
'selectdropdown1',
'selectdropdown2',
'keywordinput',
'lastcheckboxtitle1',
'lastcheckboxtitle2',
'lastcheckboxtitle3',)
@register(Abstract_0)
class abstract_1Trans(TranslationOptions):
    fields = ('title','description')


@register(Abstract_1)
class abstract_1Trans(TranslationOptions):
    fields = ('title','description','title_name')


@register(Abstract_2)
class abstract_2Trans(TranslationOptions):
    fields = ('title_name','title','description',)

@register(Abstract_3)
class abstrac_3Translation(TranslationOptions):
    fields = ('title_name','title','description',)

@register(Abstract_4)
class abstract_4Trans(TranslationOptions):
    fields = ('title_name','title','description',)

@register(Abstract_5)
class abstract_4Trans(TranslationOptions):
    fields = ('title_name','title','description',)






 

 



 



 






 
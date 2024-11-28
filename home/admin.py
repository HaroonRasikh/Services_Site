from django.contrib import admin
from menue.models import Menue,Number,Email
from .models import Photo,MainPhoto,Subject,Logo,Sponsor,Schedule,TimeDown,News,UpcomingEvent
from about.models import About,People
from program.models import Program,Event
from merzeciler.models import Maruzacilar,Maruzacilar_1
from komite.models import Komite
from gallery.models import Gallery
from xaber.models import Xaber
from modeltranslation.admin import TranslationAdmin
from sponsor.models import *
from abstract.models import *
# Register your models here.
@admin.register(Menue)
class Menuetadmin(TranslationAdmin):
      list_display = [
                    'menue_1','image','image2','menue_2','menue_3','menue_4','menue_5',
                    'menue_6','menue_7','menue_8','menue_9','menue_10','menue_11',
                    'menue_12','menue_13','menue_14','menue_15','menue_16','menue_17',
                    'menue_18','slug','menue_17','menue_18',
                    
                    ]
      list_display_links =['menue_1']
      list_editable =['image','menue_2','image2','menue_3','menue_4','menue_5',
                    'menue_6','menue_7','menue_8','menue_9','menue_10','menue_11']
      group_fieldsets =True
      class Media:
            js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
            }
      
 
@admin.register(Number)
class Numbertadmin(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Email)
class Emailtadmin(admin.ModelAdmin):
    list_display = ['email']
    


@admin.register(MainPhoto)
class Mainphotoadmin(TranslationAdmin):
    list_display = ['image_1','image_2','image_3','title','description']
    list_display_links =['title']
    list_editable = ['image_1','image_2','image_3','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Photo)
class Productadmin(TranslationAdmin):
    list_display = ['description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Subject)
class Subadmin(TranslationAdmin):
    list_display = ['title','description']
    list_editable = ['description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Schedule)
class Scheduleadmin(TranslationAdmin):
    list_display = ['name','date','title','description']
    list_editable = ['date','title','description'] 
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  




@admin.register(TimeDown)
class Mainadmin(admin.ModelAdmin):
    list_display = ['date']
    list_display_links= None
    list_editable = ['date']  
     


@admin.register(News)
class Newsadmin(TranslationAdmin):
    list_display = ['name','title','image']
    list_editable = ['title','image']  
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  


@admin.register(UpcomingEvent)
class UpcomingEvenadmin(TranslationAdmin):
    list_display = ['date','statement']
    list_display_links=None
    list_editable = ['date','statement']  
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  



@admin.register(Sponsor)
class Mainadmin(TranslationAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  












@admin.register(Logo)
class Logoadmin(TranslationAdmin):
    list_display = ['name','logo']
    list_editable =['logo']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  



'''''''''ABOUT'''''''''

@admin.register(About)
class Aboutadmin(TranslationAdmin):
    list_display = ['name','image','main_description','sub_description1','sub_description2','sub_description3']
    list_editable =['image','main_description','sub_description1','sub_description2','sub_description3']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  


@admin.register(People)
class Peopletadmin(TranslationAdmin):
    list_display = ['name','profile','about']
    list_editable =['profile','about']

    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  


# ============================should remember to translate!===============
#====================================Program==============================
from program.models import Manager
@admin.register(Program)
class Programtadmin(TranslationAdmin):
    list_display = ['name','title','description','file']
    list_editable =['title','description','file']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  
    

@admin.register(Event)
class Eventtadmin(TranslationAdmin):
    list_display = ['title','time','description']
    list_editable =['time','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  
from program.models import Event_2
@admin.register(Event_2)
class Eventtadmin(TranslationAdmin):
    list_display = ['title','time','description']
    list_editable =['time','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 

@admin.register(Manager)
class manageradmin(TranslationAdmin):
    list_display = ['name','description']
    list_editable =['description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 






'''================Maruzacilar==========='''

@admin.register(Maruzacilar)
class Maruzacilaradmin(TranslationAdmin):
     
    list_display = ['menue_name', 'name', 'profile', 'about','social1','social2','social3']
    list_editable = ['name', 'profile', 'about','social1','social2','social3' ]
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  



@admin.register(Maruzacilar_1)
class Maruzacilaradmin(TranslationAdmin):
     
    list_display = ['menue_name', 'name', 'profile', 'about','social1','social2','social3']
    list_editable = ['name', 'profile', 'about','social1','social2','social3' ]
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  


'''============Komite=============='''

@admin.register(Komite)
class Komiteadmin(TranslationAdmin):
    list_display = ['menue_name', 'name', 'profile', 'about','social1','social2','social3']
    list_editable = ['name', 'profile', 'about','social1','social2','social3' ]
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

from komite.models import Komite_1
@admin.register(Komite_1)
class Komit1eadmin(TranslationAdmin):
    list_display = ['menue_name', 'name', 'profile', 'about','social1','social2','social3']
    list_editable = ['name', 'profile', 'about','social1','social2','social3' ]
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }





'''======================Gallery==============='''

@admin.register(Gallery)
class Galleryadmin(TranslationAdmin):
    list_display = ['title_name', 'title' ,'date_detail', 'description']
    list_editable = ['title' ,'date_detail', 'description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

from gallery.models import Video
@admin.register(Video)
class videoadmin(admin.ModelAdmin):
    list_display =['video','date','date_detail']
    list_editable = ['date','date_detail']



'''======================xaber==================='''

@admin.register(Xaber)
class xabersadmin(TranslationAdmin):
    list_display = ['name','title','image']
    list_editable = ['title','image']  
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 


'''=====================sponsors=================='''

@admin.register(mainSponsor)
class sponsorsadmin(TranslationAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  
@admin.register(category1)
class sponsorsadmin(TranslationAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }  

@admin.register(category2)
class sponsorsadmin(TranslationAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 

@admin.register(category3)
class sponsorsadmin(TranslationAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 

@admin.register(category4)
class sponsorsadmin(TranslationAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }    

@admin.register(Sponsorsave)
class saveadmin(admin.ModelAdmin):
    list_display = ['name','surname','email','mobile','company_name','conference_name']


from alaqe.models import Map,Alaqe
@admin.register(Map)
class mapadmin(admin.ModelAdmin):
    list_display=['map']

@admin.register(Alaqe)
class alaqeadmin(admin.ModelAdmin):
    list_display=['name','phone_number','message']


#=========================abstracts=================
#===================================================

@admin.register(SurveyTitle)
class surveytitle(TranslationAdmin):
    list_display = ['maintitle',
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
'lastcheckboxtitle3']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Abstract_0)
class abs_0admin(TranslationAdmin):
    list_display = ['title','description']
    list_editable = ['description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Abstract_1)
class abs_1admin(TranslationAdmin):
    list_display = ['title_name','title','description']
    list_editable = ['title','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Abstract_2)
class abs_2admin(TranslationAdmin):
    list_display = ['title_name','title','description']
    list_editable = ['title','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Abstract_3)
class abs_3admin(TranslationAdmin):
    list_display = ['title_name','title','description']
    list_editable = ['title','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Abstract_4)
class abs_4admin(TranslationAdmin):
    list_display = ['title_name','title','description']
    list_editable = ['title','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Abstract_5)
class abs_4admin(TranslationAdmin):
    list_display = ['title_name','title','description']
    list_editable = ['title','description']
    group_fieldsets =True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




@admin.register(Abstract_Number)
class abstractNumber(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Abstract_Email)
class abstractEmail(admin.ModelAdmin):
    list_display = ['email']
    
@admin.register(Text)
class abstract_metin(admin.ModelAdmin):
    list_display = ['description']


#---------------------------------Anket-------------------------------
#---------------------------------------------------------------------

admin.site.register(Survey)
admin.site.register(RowSubmission)
#admin.site.register(Draft)
#admin.site.register(DraftRow_Submission)

admin.site.register(dropdown1options)
admin.site.register(dropdown2options)
admin.site.register(dropdown3options)
admin.site.register(dropdown4options)
admin.site.register(dropdown5options)

admin.site.register(selectbox1options)
admin.site.register(selectbox2options)
 
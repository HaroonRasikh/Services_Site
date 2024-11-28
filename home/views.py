from django.shortcuts import render,redirect
from menue.models import Menue,Number,Email
from .models import Photo,MainPhoto,Subject,Logo,Sponsor,TimeDown,Schedule,News,UpcomingEvent
from datetime import datetime
from about.models import About,People
from django.db.models import Q
from program.models import Program,Event
from merzeciler.models import Maruzacilar,Maruzacilar_1
from komite.models import Komite
from django.utils.translation import activate
from .forms import contactusForm 
from sponsor.models import *
from home.api_istekleri import *


def menue(request):
   selected_lang = request.GET.get('lang', None)
   if selected_lang:
         activate(selected_lang)

   mnue= Menue.objects.all()
   number = Number.objects.all()
   email = Email.objects.all()
   foto = Photo.objects.all()
   photo = MainPhoto.objects.all()
   subject= Subject.objects.all()
   logotitle = Logo.objects.first()
   logo = Logo.objects.all()
    
   sponsortitle = Sponsor.objects.first()
   sponsor = Sponsor.objects.all()
   firstschedule = Schedule.objects.first() 
   schedule = Schedule.objects.filter()[1:]

    

   
   timedowns = TimeDown.objects.first()
   if timedowns:
       times = timedowns.date.strftime('%Y-%m-%d %H:%M:%S')
   else:
       times='yok'
 
   newsname = News.objects.first()
   news1 = News.objects.all()[:6]
   news = News.objects.all()

   upcomevent = UpcomingEvent.objects.all()
   
   context = {'sponsor':sponsor,'sponsortitle':sponsortitle,
               'menue':mnue,'email':email,'number':number,'pic':foto,'mainphoto':photo,
               'subject':subject,'logotitle':logotitle,'logo':logo,'timedowns':times,'firstschedule':firstschedule,
               'schedule':schedule,'news':news,'newsname':newsname,'news1':news1,
               'upcomevent':upcomevent,'selected_lang': selected_lang,
               
               
               }
    
   return render(request,'home/esas.html',context)


def newspost(request,pk):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    number = Number.objects.all()
    email = Email.objects.all()
    mnue= Menue.objects.all()
    post = News.objects.get(id=pk)
    context={  'post':post,'menue':mnue,
               'selected_lang': selected_lang,
               'email':email,
               'number':number
             }
    return render(request,'home/newspost.html',context)



'############################Hakkinda######################'

# 

def about(request):

   selected_lang = request.GET.get('lang', None)
   if selected_lang:
         activate(selected_lang)
     
   menue = Menue.objects.all()
         
   number = Number.objects.all()
   email = Email.objects.all()
   about=About.objects.all()
   people = People.objects.all()
   context ={'about':about,'people':people, 'menue':menue,
                   'number':number,'email':email,'selected_lang': selected_lang}
   return render(request,'about/haqqimizda.html',context)
    











     

'===================program========='
from program.models import Manager,Event_2

def program(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    title = Program.objects.first()
    prgm = Program.objects.all()
    tarih= Event.objects.all()
    event2 = Event_2.objects.all()
    director=Manager.objects.all()

    context = {
                    'program':prgm,'programtitle':title,
                    'menue':menue,'number':number,
                    'email':email,'selected_lang': selected_lang,
                    'tarih':tarih,
                    'event2':event2,
                    'director':director                           
              }
    return render(request,'program/program.html',context)


'===================maruzaciler=============='

def merzeciler(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()

    merzetitle = Maruzacilar.objects.first()
    merze = Maruzacilar.objects.all()
    merze1 = Maruzacilar_1.objects.all()

    return render(request,'merzecilerkomite/merzeciler.html',{'menue':menue,'merzetitle':merzetitle,
                                             'merzeciler':merze,'number':number, 'merze1':merze1,
                                             'email':email,'selected_lang': selected_lang})


'''===================komite=============='''

from komite.models import Komite_1

def komite(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()

    komitetitle = Komite.objects.first()
    kmte = Komite.objects.all()
    komte1 = Komite_1.objects.all()
    return render(request,'merzecilerkomite/komite.html',{'menue':menue,'komitetitle':komitetitle,
                                         'kmte':kmte,'number':number,
                                         'email':email,'selected_lang': selected_lang,
                                         'komite1':komte1,
                                         })


'''======================sponsorposts====================='''

# def sponsorpost(request):
#     #post = News.objects.get(id=pk)
#     sponsortitle = Sponsor.objects.first()
#     sponsor = Sponsor.objects.all()
#     context = {'sponsor':sponsor,'sponsortitle':sponsortitle}
#     return render(request,'sponsorlar.html',context)









''' =========================search=============================== '''

def search(request):
      selected_lang = request.GET.get('lang', None)
      if selected_lang:
             activate(selected_lang)
      menue = Menue.objects.all()
      search_text = request.GET.get('searched')
      foto =   []
      subject =[]
      schedule =[]
      abouttitle=[]
      model1 = []
      model2 = []
      firstschedule =[]
      newsname = []
      news1 = []
      maruzaci1=[]
      maruzaci2=[]
      sponsortitle=[]
      sponsor=[]
      mainphoto=[]
      upcomingevent=[]

      maruzaci1title=[]
      maruzaci2title=[]
      komite1 =[]
      komite1title=[]
      komite2=[]
      komite2title=[]
    

      programtitle=[]
      program1 = []
      program2title=[]
      program2=[]
      program3title=[]
      program3=[]
      
      program4=[]
      abstract0=[]
      abstract1=[]
      abstract2=[]
      abstract3=[]
      abstract4=[]
      abstract5=[]

      if search_text:
           
           mainphoto= MainPhoto.objects.filter(Q(title__contains=search_text)|Q(description__contains=search_text))
           
           newsname = News.objects.filter(Q(name__contains=search_text)).first()
           news1 = News.objects.filter(Q(title__contains=search_text))
           upcomingevent=UpcomingEvent.objects.filter(Q(date__contains=search_text)|Q(statement__contains=search_text)) 
           firstschedule = Schedule.objects.filter(Q(name__contains=search_text)).first()
           foto = Photo.objects.filter(Q(description__contains=search_text))
           subject= Subject.objects.filter(Q(title__contains=search_text)|Q(description__contains=search_text))
           schedule = Schedule.objects.filter(Q(date__contains=search_text)|Q(title__contains=search_text)|Q(description__contains=search_text)) 
           sponsortitle=mainSponsor.objects.filter(Q(name__contains=search_text)).first()
           sponsor= mainSponsor.objects.filter(Q(description__contains=search_text))
           
           
           abouttitle=About.objects.filter(Q(name__contains=search_text)).first()
           model1 = About.objects.filter(Q(name__contains=search_text)|Q(main_description__contains=search_text)|Q(sub_description1__contains = search_text)|
                                      Q(sub_description2__contains = search_text)|Q(sub_description3__contains = search_text) )
           model2 = People.objects.filter(Q(name__contains=search_text)|Q(about__contains=search_text))
           maruzaci1title= Maruzacilar.objects.filter(Q(menue_name__contains=search_text)).first()
           maruzaci1 = Maruzacilar.objects.filter(Q(name__contains=search_text)|Q(about__contains=search_text))
           maruzaci2title = Maruzacilar_1.objects.filter(Q(menue_name__contains=search_text)).first()
           maruzaci2 = Maruzacilar_1.objects.filter(Q(name__contains=search_text)|Q(about__contains=search_text))
           komite1title= Komite.objects.filter(Q(menue_name__contains=search_text)).first()
           komite1 = Komite.objects.filter(Q(name__contains=search_text)|Q(about__contains=search_text))
           komite2title= Komite_1.objects.filter(Q(menue_name__contains=search_text)).first()
           komite2 = Komite_1.objects.filter(Q(name__contains=search_text)|Q(about__contains=search_text))

           programtitle= Program.objects.filter(Q(name__contains=search_text)).first()
           program1=Program.objects.filter(Q(title__contains=search_text)|Q(description__contains=search_text))
           program2title=Event.objects.filter(Q(title__contains=search_text)).first()
           program2=Event.objects.filter(Q(time__contains=search_text)|Q(description__contains=search_text))
           
           program3title=Event_2.objects.filter(Q(title__contains=search_text)).first()
           program3=Event_2.objects.filter(Q(time__contains=search_text)|Q(description__contains=search_text))
           program4=Manager.objects.filter(Q(name__contains=search_text)|Q(description__contains=search_text))

           abstract0=Abstract_0.objects.filter(Q(title__contains=search_text)|Q(description__contains=search_text))
           abstract1=Abstract_1.objects.filter(Q(title_name__contains=search_text)|Q(title__contains=search_text)|Q(description__contains=search_text))
           abstract2=Abstract_2.objects.filter(Q(title_name__contains=search_text)|Q(title__contains=search_text)|Q(description__contains=search_text))
           abstract3=Abstract_3.objects.filter(Q(title_name__contains=search_text)|Q(title__contains=search_text)|Q(description__contains=search_text))
           abstract4=Abstract_4.objects.filter(Q(title_name__contains=search_text)|Q(title__contains=search_text)|Q(description__contains=search_text))
           abstract5=Abstract_5.objects.filter(Q(title_name__contains=search_text)|Q(title__contains=search_text)|Q(description__contains=search_text))
           #maruzaci1 = Maruzacilar.objects.filter(Q(name_contains=search_text)|
            #                                      Q(about_contains=search_text))
          #maruzaci2 = Maruzacilar_1.objects.filter(Q(menue_name_contains=search_text)|Q(name_contains=search_text)|
           #                                       Q(about_contains=search_text))
           
     


 
      mnue= Menue.objects.all()
      number = Number.objects.all()
      email = Email.objects.all() 
      context ={  'about':model1,'people':model2,'menue':menue,
                   'mainphoto':mainphoto,
                  'subject':subject,'pic':foto,'schedule':schedule,
                  'firstschedule':firstschedule,'newsname':newsname,
                  'news1':news1,'maruzaci1':maruzaci1,'maruzaci2':maruzaci2,
                  'sponsor':sponsor,
                   'sponsortitle':sponsortitle,
                   'upcomevent':upcomingevent,
                   'abouttitle':abouttitle,
                    'selected_lang': selected_lang,
                    'maruzaci1title':maruzaci1title,
                    'maruzaci2title':maruzaci2title,
                    'komite1':komite1,
                    'komite1title':komite1title,
                    'komite2':komite2,
                    'komite2title':komite2title,

                    'programtitle':programtitle,
                    'program1':program1,
                    'program2title':program2title,
                    'program2':program2,
                    'program3title':program3title,
                    'program3':program3,
                    'program4':program4,
                    'abstract0':abstract0,
                    'abstract1':abstract1,
                    'abstract2':abstract2,
                     'abstract3':abstract3,
                     'abstract4':abstract4,
                     'abstract5':abstract5,
                     'menue':mnue,'email':email,'number':number,

                
                
                
            }
      return render(request,'search.html',context)

def searchposts(request,pk ):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    post1 = About.objects.get(id=pk)
    post2 = People.objects.get(id=pk)
   
    context = {'post1':post1,'post2':post2}
    
    return render(request,'searchpost.html',context)





'''====================qeydiyyat=================='''

def qeydiyyat(request):
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    return render (request,'abstrakt.qeydiyyat.html',{'menue':menue,
'number':number,'email':email})


 
    

 





''''===========================APIlogin ======================'''



from django.conf import settings
import httpx
from django.shortcuts import render, redirect

AUTH_API_URL = 'https://api.uimconsulting.com/en/v2/auths'

def login_view(request):
    message = ''
    if request.method == 'POST':
        # Get the username and password from the form data
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        # Send the login request to the API
        response = httpx.post(AUTH_API_URL, json={'username': username, 'password': password})

        # If the login was successful, redirect to the about page
        if response.status_code == 200:
            response = response.json()
            message = response['message']
            
            #print(response.json())
            #return redirect('/')
        
        else:
            # If the login failed, display an error message on the login page
            error_message = 'Invalid credentials'
            return render(request, 'signin.html', {'error_message': error_message})
    
        # If the request method is GET, display the login page

    context ={'error_message':message}
    return render(request, 'signin.html',context)




'''==============Gallery==============='''




from gallery.models import Gallery
def galerry(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)

    mnue= Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    images = Gallery.objects.all()

    contex =    {
                    'menue':mnue,
                    'number':number,
                    'email':email,
                    'gallery':images,
                    'selected_lang': selected_lang,

                }
    return render(request,'gallery/fotolar.html',contex)



'''==================gallerypost============ '''



def gallerypost(request,pk):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)

    mnue= Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    images = Gallery.objects.all()

    gallerypost = Gallery.objects.get(id=pk)
    images = Gallery.objects.all()
    
    context = { 
                'menue':mnue,
                'number':number,
                'email':email,
                'gallerypost':gallerypost,
                'gallery':images,
              'selected_lang': selected_lang,
              }
    
    return render(request,'gallery/fotolar2.html',context)

from gallery.models import Video

def youtube(request):
    mnue= Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    youtube= Video.objects.all()

    context = {
                 'menue':mnue,
                'number':number,
                'email':email,
                 'youtube':youtube
                }

    return render(request,'gallery/video.html',context)


'''===========mainsponsors========
=================================='''
from .forms import sponsorform

def sponsors(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)

    mnue= Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
   
    
    main = mainSponsor.objects.all()
    sponsor1= category1.objects.all()
    sponsor2=category2.objects.all()
    sponsor3=category3.objects.all()
    sponsor4=category4.objects.all()
    gondermessage = False
   
    # if request.method == 'POST':
    #     ad = request.POST.get('name')
    #     soyad = request.POST.get('lastname')
    #     email = request.POST.get('email')
    #     mobile = request.POST.get('number')
    #     company = request.POST.get('company')
    #     conference = request.POST.get('konferans')
    #     keyt = Sponsorsave( name=ad,surname=soyad,
    #                         email=email,mobile=mobile,
    #                         company_name=company,
    #                         conference_name=conference,   
                           
    #                        )
    #     keyt.save()
    receiver_emails=Email.objects.values_list('email', flat=True)
    if request.method == 'POST':
        form = sponsorform(request.POST)
        if form.is_valid():
            sponsor='SPONSOR'
            Name = form.cleaned_data['Name']
            Surname = form.cleaned_data['Surname']
            Emailform = form.cleaned_data['Emailform']
            Mobile = form.cleaned_data['Mobile']
            Company = form.cleaned_data['Company']
            Conference = form.cleaned_data['Conference']
            keyt = Sponsorsave( name=Name,surname=Surname,
                             email=Emailform,mobile=Mobile,
                             company_name=Company,
                             conference_name=Conference   
                           
                            )
            keyt.save()
            msg = "Ad:    {0}\nSoyad:     {1}\nEmail:   {2}\nMobile:    {3}\nCompany:    {4}\nConference:   {5}\n".format(Name,Surname,Emailform,Mobile,Company,Conference)
            print(msg)
            send_mail(
                sponsor,
                msg,
                settings.EMAIL_HOST_USER, 
                receiver_emails,
               # ['mohammadharoonmozafary@gmail.com'],
                fail_silently=False,
                
            )
            gondermessage =True 
           
            context = {  
                 'form':form,
                 'sent':gondermessage,
                    'menue':mnue,
                    'number':number,
                    'email':email,
                    'sponsor':main,
                    'sponsor1':sponsor1,
                    'sponsor2':sponsor2,
                    'sponsor3':sponsor3,
                    'sponsor4':sponsor4,
                    'selected_lang': selected_lang,
                    

              }
            return render(request,'sponsorlar.html',context)
    form = sponsorform()
    context = {  
                 'form':form,
                 'sent':gondermessage,
                    'menue':mnue,
                    'number':number,
                    'email':email,
                    'sponsor':main,
                    'sponsor1':sponsor1,
                    'sponsor2':sponsor2,
                    'sponsor3':sponsor3,
                    'sponsor4':sponsor4,
                    

              }
    return render(request,'sponsorlar.html',context) 


    

 


'''================xaber====================
==============================================='''


from xaber.models import Xaber
def xabers(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)

    mnue= Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    mainxaber= Xaber.objects.all()

    context = { 'menue':mnue,
                'number':number,
                'email':email,
                'xaber':mainxaber,
                'selected_lang': selected_lang,
            }
    return render(request,'xaber/xeberler2.html',context)

def mainxaberpost(request,pk):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)

    mnue= Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    
    mainxaberpost = Xaber.objects.get(id=pk)
    context = { 'menue':mnue,
                'number':number,
                'email':email,
                'selected_lang': selected_lang,
                'mainpost':mainxaberpost,
            }
    return render(request,'xaber/mainxaberpost.html',context)

'''======================alaqa===================
===================================================
'''


from django.core.mail import send_mail
from django.conf import settings
from alaqe.models import Map,Alaqe

#from .forms import contactusForm


def alaqa(request):
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    harite= Map.objects.first()
    send = False
    receiver_emails=Email.objects.values_list('email', flat=True)
    if request.method == 'POST':
        form = contactusForm(request.POST)
        if form.is_valid():
            contact='ALAQA'
            Name = form.cleaned_data['Name']
            Mobile_number = form.cleaned_data['Mobile_number']
            Message = form.cleaned_data['Message']
            keyt=Alaqe(name=Name,phone_number=Mobile_number,message=Message)
            keyt.save()
            msg = "Ad:    {0}\nNumara:     {1}\nMesaj:   {2}\n".format(Name,Mobile_number,Message)
            print(msg)
            send_mail(
                contact,
                msg,
                settings.EMAIL_HOST_USER, 

                receiver_emails,
              #  ['mohammadharoonmozafary@gmail.com'],
                fail_silently=False,
                
            )
            send =True 
            return render(request,'elaqe.html',{'form':form,'sent':send,'menue':menue,'number':number,'email':email})
    
    form = contactusForm()
    return render(request,'elaqe.html',{'form':form,'menue':menue,
                                       'number':number,'email':email,
                                       'harite':harite,
                                       'sent':send
                                    })  
     





#==========================API==========================
#=======================================================
#========================================================


def sign_in(request):
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()

    if 'access_token' in request.session:
        return redirect('survey')

    error_message = ''

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        signing_in_request = try_signing_in(email, password, request)

        if signing_in_request.get('access_token'):
            request.session['username'] = email
            request.session['password'] = password
            return redirect('survey')
        else:
            error_message = signing_in_request['message']
            
    context = {
        'error_message': error_message,
                'menue':menue,
                'number':number,
                'email':email,
            
    }
    return render(request, 'users/abstrakt.qeydiyyat.html', context)

def sign_out(request):
    if request.session.get('access_token'):
        del request.session['access_token']
    
    return redirect('sign_in')

def sign_up(request):
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    error_message = ''
    if 'access_token' in request.session:
        return redirect('survey')


    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        fullname = request.POST['fullname']
        idcard = request.POST['idcard']

        signing_up_request = try_signing_up(email,phone, password,fullname,idcard)
         
        if signing_up_request.get('success'):
            return redirect('confirm')
        #if signing_up_request.get('access_token'):
         #   request.session['access_token'] = signing_up_request['access_token']
          #  return redirect('home')
        else:
            error_message = signing_up_request['message']
        
    context = {
        'error_message': error_message,
        'menue':menue,
        'number':number,
        'email':email,
            
    }
    return render(request, 'users/abstrakt.qeydiyyat.html', context)

def authenticated(request):
      return 'access_token' in request.session


def confirm(request):
    if authenticated(request) ==True:
        return redirect('home')
    
    return render(request,'confirm_account.html')



def profiledetail(request):
   if 'access_token' not in request.session:
        return redirect('sign_in')  
   menue = Menue.objects.all()
   number = Number.objects.all()
   email = Email.objects.all()
   context = {'menue':menue,
                'number':number,
                'email':email,}
   response = getUserDetails(request)
   if response.get('success'):
       context['currentUser'] = response['currentUser']
   return render(request,'users/detail.html', context)


def updateProfile(request):
    if 'access_token' not in request.session:
        return redirect('sign_in')  
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    context = {'menue':menue,
                'number':number,
                'email':email,}    
    response = getUserDetails(request)
    if response.get('success'):
       context['currentUser'] = response['currentUser']
    
    if request.method == 'POST':
        formData = {
                        'fullname': request.POST['fullname'],
                        'idcard': request.POST['idcard'],
                        'phone': request.POST['phone'],
                        # 'type': request.POST['type'],
                        # 'workplace': request.POST['workplace'],
                        # 'speciality': request.POST['speciality'],
                 }
        
        if len(request.POST['birthdate']) == 0:
            formData['birthdate'] = '0000.00.00' 
        else:
            formData['birthdate'] = str(request.POST['birthdate']).replace('-', '.')

        request_result = update_request(formData, request)
        if request_result.get('success') != None:
            return redirect('detail')
        else:
            context['error_message'] = request_result['message']

    return render(request, 'users/updateProfile.html', context)
from django.http import HttpResponseNotAllowed,HttpResponse
import httpx
import json

def change_password(request):
    if 'access_token' not in request.session:
        return redirect('sign_in')  
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    context = {'menue':menue,
                'number':number,
                'email':email,}
    # Send Request to our API endpoint.
    if request.method == 'POST':
        current_password = request.POST.get('current_password')    
        new_password = request.POST.get('new_password')    
        changing_password_request = change_password_request(current_password, new_password, request)
        if 'success' in changing_password_request:
            context['error_message'] = 'Your password was updated successfully!'
            request.session['password'] = new_password
        else:
            context['error_message'] = changing_password_request['message']
    # Show change password form
    elif request.method == 'GET':
        pass
    else:
        return HttpResponseNotAllowed()
    
    return render(request, 'users/change_password.html', context)



#=======================ABSTRACTLAR====================
#======================================================
from abstract.models import *
def abstract(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    abstract_0 = Abstract_0.objects.all()
    abstrct_1= Abstract_1.objects.all()
    Abstract_1_first = Abstract_1.objects.first()
    
    abstrct_2 = Abstract_2.objects.all()
    Abstract_2_first = Abstract_2.objects.first()


    abstrct_3 = Abstract_3.objects.all()
    Abstract_3_first= Abstract_3.objects.first()

    abstrct_4 = Abstract_4.objects.all()
    Abstract_4_first= Abstract_4.objects.first()

    abstract_5 = Abstract_5.objects.all()
    Abstract_5_first= Abstract_5.objects.first()
    

    abstract_phone = Abstract_Number.objects.all()
    abstract_email = Abstract_Email.objects.all()
    
    mainxaber= Xaber.objects.all()
    text=Text.objects.all()
   
    context = { 'menue':menue,
                'number':number,
                'email':email,
                'abstract_0':abstract_0,
                'abstract_1':abstrct_1,
                'first':Abstract_1_first,

                'abstract_2':abstrct_2,
                'first_2':Abstract_2_first,
                
                'abstract_3':abstrct_3,
                'first_3':Abstract_3_first,

                'abstract_4':abstrct_4,
                 'first_4':Abstract_4_first,

                'abstract_5':abstract_5,
                 'first_5':Abstract_5_first,


                 'xaber':mainxaber,
                'abstract_phone':abstract_phone,
                'abstract_email':abstract_email,
                'text':text,
                'selected_lang': selected_lang,
            }

    return render(request,'abstract/abstrakt.online.html',context)

def abstractanket(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()

    context = { 'menue':menue,
                'number':number,
                'email':email,
                'selected_lang': selected_lang,
            }
    
    if 'access_token' not in request.session:
        return redirect('sign_in')   

 
    return render(request,'abstract/abstract.sub.html',context)

#-----------------------------------------------------------------------------------------
#---------------------------------------ANKET KEYITTI-------------------------------------
#-----------------------------------------------------------------------------------------

from django.core.mail import EmailMultiAlternatives  # ----1
from django.template.loader import render_to_string
from django.utils.html import strip_tags 
from django.core.mail import send_mail
from .models import *
from django.http import HttpResponse
from django.conf import settings
#------------------------Survey---------------------------
#---------------------------------------------------------

def survey(request):
    selected_lang = request.GET.get('lang', None)
    if selected_lang:
         activate(selected_lang)
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    survey_title=SurveyTitle.objects.first()
    mainxaber= Xaber.objects.all()

    if 'access_token' not in request.session:
        return redirect('sign_in')  
    if request.method == 'POST':
        # Get the submitted cities, countries, and dropdown options
        textbox1 = request.POST.get('textbox1')
        dropdown1_id = request.POST.get('dropdown1')
        dropdown2_id = request.POST.get('dropdown2')
        dropdown3_id = request.POST.get('dropdown3')
        dropdown4_id = request.POST.get('dropdown4')

        dropdown6_id = request.POST.get('dropdown6')
        dropdown7_id = request.POST.get('dropdown7')

        dropdown1=dropdown1options.objects.get(id=dropdown1_id)
        dropdown2 = dropdown2options.objects.get(id=dropdown2_id)
        dropdown3=dropdown3options.objects.get(id=dropdown3_id)
        dropdown4 = dropdown4options.objects.get(id=dropdown4_id)

        dropdown6 = selectbox1options.objects.get(id=dropdown6_id)
        dropdown7=selectbox2options.objects.get(id=dropdown7_id)
        email2 = request.session['username']
        


        
        select1 = request.POST.get('select1')=='on'
        textbox2 = request.POST.get('textbox2')
        select2 = request.POST.get('select2') == 'on'
        
        #===========add row==============================
        dropdown5_id = request.POST.getlist('dropdown5_id[]')
       # dropdown5=dropdown5options.objects.get(id=dropdown5_id[0])

        lastname = request.POST.getlist('lastname[]')
        firstname= request.POST.getlist('firstname[]')
        firstname_init= request.POST.getlist('firstname_init[]')
        email = request.POST.getlist('email[]')
        affilation= request.POST.getlist('affiliation[]')
        city= request.POST.getlist('city[]')
        country= request.POST.getlist('country[]')


        background = request.POST.get('background')
        method = request.POST.get('method')
        result = request.POST.get('result')
        conclusion = request.POST.get('conclusion')
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        file3 = request.FILES.get('file3')
        print('files before submiting!',file1,file2,file2)
        keyword_1 = request.POST.get('keyword_1')
        checkbox_1 = request.POST.get('checkbox_1') == 'on'
        checkbox_2 = request.POST.get('checkbox_2') == 'on'
        checkbox_3 = request.POST.get('checkbox_3') == 'on'

        if len(lastname) >= 1 and len(firstname)and len(email)and len(firstname_init)and len(affilation)and len(city)and len(country) >= 1:
            # Save the survey in Surveyy
            print('testing files:',file1,file2,file3)
            survy =Survey(
               textbox1=textbox1,dropdown_1=dropdown1,dropdown_2=dropdown2,dropdown_3=dropdown3,
            dropdown_4=dropdown4,dropdown_5=dropdown5options.objects.get(id=dropdown5_id[0]), selectbox_1=dropdown6,selectbox_2=dropdown7,
                                select1=select1,
                                textbox2=textbox2,select2=select2,
                                lastname=lastname[0],name=firstname[0],
                                email=email[0],first_name_init=firstname_init[0],
                                affilation=affilation[0],city=city[0],country=country[0],

                                background=background,method=method,result=result,
                                conclusion=conclusion,file_1=file1, file_2=file2,file_3=file3,
                                keyword_1=keyword_1,checkbox_1=checkbox_1,checkbox_2=checkbox_2,
                                checkbox_3=checkbox_3
                
            )
            survy.save()
        
            print('testing',survy.lastname)
            
            for i in range(1, len(lastname)):
                if edit_draft: 
                    dropdown5=dropdown5options.objects.get(id=dropdown5_id[i-2])
                else:
                    dropdown5=dropdown5options.objects.get(id=dropdown5_id[i])

                row=RowSubmission(
                    survey=survy,
                    lastname=lastname[i],
                    name=firstname[i],
                    email=email[i],
                    first_name_init=firstname_init[i],
                    affilation=affilation[i],
                    city=city[i],
                    country=country[i],
                    dropdown_5=dropdown5,
                    email2=email2
                   )
                row.save()
        
                
            roww=RowSubmission.objects.filter(survey=survy)
            html_content = render_to_string("survey/email_template.html",{'title':'test_mail','survey':survy,'form_data':roww,'survey_title':survey_title})
            print('testing row',RowSubmission.first_name_init)
            text_content =strip_tags(html_content)
            receiver_emails=Email.objects.values_list('email', flat=True)
            email=EmailMultiAlternatives(
                  "ANKET", #subject,
                   text_content ,
                   settings.EMAIL_HOST_USER,
                  receiver_emails)
             #   text content #content 
              #  sfsf@gmailcom#from email 
               # sdfsdf@gmail.com#rec list
            #)
            email.attach_alternative(html_content,"text/html")
            email.send()

                

        # Determine if the survey should be saved in Surveyy or Location
        else:
            return HttpResponse("At least one city and country must be provided.")

        return render(request,'survey/thanks.html')

    # Get all the dropdown options for the form
    options1 = dropdown1options.objects.all()
    options2 = dropdown2options.objects.all()
    options3 = dropdown3options.objects.all()
    options4 = dropdown4options.objects.all()
    options5 = dropdown5options.objects.all()
    selectoption1 = selectbox1options.objects.all()
    selectoption2 = selectbox2options.objects.all()
    abstract_phone = Abstract_Number.objects.all()
    abstract_email = Abstract_Email.objects.all()
    text=Text.objects.all()
    context= {
                    'option1':options1,
                    'option2':options2,
                    'option3':options3,
                    'option4':options4,
                    'option5':options5,
                    'selectoption1':selectoption1,
                    'selectoption2':selectoption2,
                    'menue':menue,
                    'number':number,
                    'email':email,
                    'xaber':mainxaber,
                    'abstract_phone':abstract_phone,
                    'abstract_email':abstract_email,
                    'survey_title':survey_title,
                    'text':text,
                    'selected_lang': selected_lang,
             }
    return render(request, 'survey/survey.html',context)


 #----------------------Preview Survey-----------------
 #-----------------------------------------------------

def preview(request):
    if 'access_token' not in request.session:
       return redirect('sign_in')
    survey_title=SurveyTitle.objects.first() 
    if request.method == 'POST':
        # Get the submitted cities, countries, and dropdown options
        textbox1 = request.POST.get('textbox1')
        dropdown1_id = request.POST.get('dropdown1')
        dropdown2_id = request.POST.get('dropdown2')
        dropdown3_id = request.POST.get('dropdown3')
        dropdown4_id = request.POST.get('dropdown4')

        dropdown6_id = request.POST.get('dropdown6')
        dropdown7_id = request.POST.get('dropdown7')

        dropdown1=dropdown1options.objects.get(id=dropdown1_id)
        dropdown2 = dropdown2options.objects.get(id=dropdown2_id)
        dropdown3=dropdown3options.objects.get(id=dropdown3_id)
        dropdown4 = dropdown4options.objects.get(id=dropdown4_id)

        dropdown6 = selectbox1options.objects.get(id=dropdown6_id)
        dropdown7=selectbox2options.objects.get(id=dropdown7_id)
        select1 = request.POST.get('select1')=='on'
        textbox2 = request.POST.get('textbox2')
        select2 = request.POST.get('select2') == 'on'
        
        #===========add row==============================
        dropdown5_id = request.POST.getlist('dropdown5_id[]')
        lastname = request.POST.getlist('lastname[]')
        firstname= request.POST.getlist('firstname[]')
        firstname_init= request.POST.getlist('firstname_init[]')
        email = request.POST.getlist('email[]')
        affilation= request.POST.getlist('affiliation[]')
        city= request.POST.getlist('city[]')
        country= request.POST.getlist('country[]')


        background = request.POST.get('background')
        method = request.POST.get('method')
        result = request.POST.get('result')
        conclusion = request.POST.get('conclusion')
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        file3 = request.FILES.get('file3')
        print('files before submiting!',file1,file2,file2)
        keyword_1 = request.POST.get('keyword_1')
        checkbox_1 = request.POST.get('checkbox_1') == 'on'
        checkbox_2 = request.POST.get('checkbox_2') == 'on'
        checkbox_3 = request.POST.get('checkbox_3') == 'on'

        form_data = {

            'textbox1':textbox1,
             'dropdown_1':dropdown1,
             'dropdown_2':dropdown2,
             'dropdown_3':dropdown3,
             'dropdown_4':dropdown4,
                'selectbox_1':dropdown6,
                'selectbox_2':dropdown7,
                'select1':select1,
                'textbox2':textbox2,
                'select2':select2,
                           
                           
                'lastname':lastname[0] if len(lastname) >= 1 else None ,
                'name':firstname[0] if len(firstname) >= 1 else None ,
                'email':email[0] if len(email) >= 1 else None ,
                'first_name_init':firstname_init[0] if len(firstname_init) >= 1 else None ,
                'affilation':affilation[0] if len(affilation) >= 1 else None ,
                'city':city[0] if len(city) >= 1 else None ,
                'country':country[0] if len(country) >= 1 else None ,
                'dropdown_5': dropdown5_id[0] if len(dropdown5_id) >= 1 else None,

                'background':background,
                'method':method,
                'result':result,
                'conclusion':conclusion,
                'file_1':file1,
                'file_2':file2,
                'file_3':file3,
                'keyword_1':keyword_1,
                'checkbox_1':checkbox_1,
                'checkbox_2':checkbox_2,
                'checkbox_3':checkbox_3,
            'additional_locations': []
        }
        
    

       
        for i in range(1, len(lastname)):
                dropdown5=dropdown5options.objects.get(id=dropdown5_id[i])

                additional_location = {                 
                   
                    'lastname':lastname[i],
                    'name':firstname[i],
                    'email':email[i],
                    'first_name_init':firstname_init[i],
                    'affilation':affilation[i],
                    'city':city[i],
                    'country':country[i],
                    'dropdown_5':dropdown5
                }
                form_data['additional_locations'].append(additional_location)
        
   
        return render(request, 'survey/preview.html', {'form_data': form_data,'survey_title':survey_title})
        

    # Get all the dropdown options for the form
    options1 = dropdown1options.objects.all()
    options2 = dropdown2options.objects.all()
    options3 = dropdown3options.objects.all()
    options4 = dropdown4options.objects.all()
    options5 = dropdown5options.objects.all()
    selectoption1 = selectbox1options.objects.all()
    selectoption2 = selectbox2options.objects.all()
            
    context= {
                    'option1':options1,
                    'option2':options2,
                    'option3':options3,
                    'option4':options4,
                    'option5':options5,
                    'selectoption1':selectoption1,
                    'selectoption2':selectoption2,
                    
             }
    return render(request, 'survey/preview.html',context)


#-----------------------Draft--------------
#------------------------------------------
def draft(request):

    if 'access_token' not in request.session:
       return redirect('sign_in') 
    if request.method == 'POST':
        # Get the submitted cities, countries, and dropdown options
        textbox1 = request.POST.get('textbox1')
        dropdown1_id = request.POST.get('dropdown1')
        dropdown2_id = request.POST.get('dropdown2')
        dropdown3_id = request.POST.get('dropdown3')
        dropdown4_id = request.POST.get('dropdown4')

        dropdown6_id = request.POST.get('dropdown6')
        dropdown7_id = request.POST.get('dropdown7')

        dropdown1=dropdown1options.objects.get(id=dropdown1_id)
        dropdown2 = dropdown2options.objects.get(id=dropdown2_id)
        dropdown3=dropdown3options.objects.get(id=dropdown3_id)
        dropdown4 = dropdown4options.objects.get(id=dropdown4_id)

        dropdown6 = selectbox1options.objects.get(id=dropdown6_id)
        dropdown7=selectbox2options.objects.get(id=dropdown7_id)
        
        
        select1 = request.POST.get('select1')=='on'
        textbox2 = request.POST.get('textbox2')
        select2 = request.POST.get('select2') == 'on'
        
        #===========add row==============================
        dropdown5_id = request.POST.getlist('dropdown5_id[]')
       # dropdown5=dropdown5options.objects.get(id=dropdown5_id[0])

        lastname = request.POST.getlist('lastname[]')
        firstname= request.POST.getlist('firstname[]')
        firstname_init= request.POST.getlist('firstname_init[]')
        email = request.POST.getlist('email[]')
        affilation= request.POST.getlist('affiliation[]')
        city= request.POST.getlist('city[]')
        country= request.POST.getlist('country[]')


        background = request.POST.get('background')
        method = request.POST.get('method')
        result = request.POST.get('result')
        conclusion = request.POST.get('conclusion')
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        file3 = request.FILES.get('file3')

        keyword_1 = request.POST.get('keyword_1')
        checkbox_1 = request.POST.get('checkbox_1') == 'on'
        checkbox_2 = request.POST.get('checkbox_2') == 'on'
        checkbox_3 = request.POST.get('checkbox_3') == 'on'
        email2 = request.session['username']
        if len(lastname) >= 1 and len(firstname)and len(email)and len(firstname_init)and len(affilation)and len(city)and len(country) >= 1:
            # Save the survey in Surveyy
            survy =Draft(
               textbox1=textbox1,dropdown_1=dropdown1,dropdown_2=dropdown2,dropdown_3=dropdown3,
            dropdown_4=dropdown4,dropdown_5=dropdown5options.objects.get(id=dropdown5_id[0]), selectbox_1=dropdown6,selectbox_2=dropdown7,
                                select1=select1,
                                textbox2=textbox2,select2=select2,
                                lastname=lastname[0],name=firstname[0],
                                email=email[0],first_name_init=firstname_init[0],
                                affilation=affilation[0],city=city[0],country=country[0],

                                background=background,method=method,result=result,
                                conclusion=conclusion,file_1=file1, file_2=file2,file_3=file3,
                                keyword_1=keyword_1,checkbox_1=checkbox_1,checkbox_2=checkbox_2,
                                checkbox_3=checkbox_3,email2=email2
            )
            survy.save()
            for i in range(1, len(lastname)):
                # if edit_draft:
                #     dropdown5=dropdown5options.objects.get(id=dropdown5_id[i-1])
                # else:
                dropdown5=dropdown5options.objects.get(id=dropdown5_id[i])

                DraftRow_Submission.objects.create(
                    survey=survy,
                    lastname=lastname[i],
                    name=firstname[i],
                    email=email[i],
                    first_name_init=firstname_init[i],
                    affilation=affilation[i],
                    city=city[i],
                    country=country[i],
                    dropdown_5=dropdown5
                   )
                

        # Determine if the survey should be saved in Surveyy or Location
        else:
            return HttpResponse("At least one city and country must be provided.")

        return HttpResponse('Anket göndərildi, təşəkkür edirəm!')

    # Get all the dropdown options for the form
    options1 = dropdown1options.objects.all()
    options2 = dropdown2options.objects.all()
    options3 = dropdown3options.objects.all()
    options4 = dropdown4options.objects.all()
    options5 = dropdown5options.objects.all()
    selectoption1 = selectbox1options.objects.all()
    selectoption2 = selectbox2options.objects.all()
            
    context= {
                    'option1':options1,
                    'option2':options2,
                    'option3':options3,
                    'option4':options4,
                    'option5':options5,
                    'selectoption1':selectoption1,
                    'selectoption2':selectoption2,
             }
    return render(request, 'survey/survey.html',context)
#-----------------Draft List--------------------
#----------------------------------------------
def draft_list(request):
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    if 'access_token' not in request.session:
       return redirect('sign_in') 
    drafts = Draft.objects.filter(email2=request.session['username'])
    #drafts = Draft.objects.all()
    if not drafts:  # Check if drafts list is empty
        return redirect('survey') 
    
    context=    {
                   'menue':menue,
                    'number':number,
                    'email':email,
                    'drafts': drafts
                }
    return render(request, 'survey/draft_list.html',context)

#------------------------Edit Draft----------------------
#--------------------------------------------------------
def edit_draft(request, draft_id):
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    if 'access_token' not in request.session:
       return redirect('sign_in') 
    draft = Draft.objects.get(id=draft_id)

    if request.method == 'POST':
        dropdown1_id = request.POST.get('dropdown1')
        dropdown2_id = request.POST.get('dropdown2')
        dropdown3_id = request.POST.get('dropdown3')
        dropdown4_id = request.POST.get('dropdown4')

        dropdown6_id = request.POST.get('dropdown6')
        dropdown7_id = request.POST.get('dropdown7')

        draft.dropdown_1=dropdown1options.objects.get(id=dropdown1_id)
        draft.dropdown_2 = dropdown2options.objects.get(id=dropdown2_id)
        draft.dropdown_3=dropdown3options.objects.get(id=dropdown3_id)
        draft.dropdown_4 = dropdown4options.objects.get(id=dropdown4_id)

        draft.selectbox_1 = selectbox1options.objects.get(id=dropdown6_id)
        draft.selectbox_2=selectbox2options.objects.get(id=dropdown7_id)
        
        draft.textbox1 = request.POST.get('textbox1')
        draft.select1 = request.POST.get('select1')=='on'
        draft.textbox2 = request.POST.get('textbox2')
        draft.select2 = request.POST.get('select2') == 'on'
        
        #===========add row==============================
        
        dropdown5_id = request.POST.getlist('dropdown5_id[]')
        lastname = request.POST.getlist('lastname[]')
        firstname= request.POST.getlist('firstname[]')
        firstname_init= request.POST.getlist('firstname_init[]')
        email = request.POST.getlist('email[]')
        affilation= request.POST.getlist('affiliation[]')
        city= request.POST.getlist('city[]')
        country= request.POST.getlist('country[]')


        draft.background = request.POST.get('background')
        draft.method = request.POST.get('method')
        draft.result = request.POST.get('result')
        draft.conclusion = request.POST.get('conclusion')
        draft.file_1 = request.FILES.get('file1')
        draft.file_2 = request.FILES.get('file2')
        draft.file_3 = request.FILES.get('file3')
        draft.keyword_1 = request.POST.get('keyword_1')
        draft.checkbox_1 = request.POST.get('checkbox_1') == 'on'
        draft.checkbox_2 = request.POST.get('checkbox_2') == 'on'
        draft.checkbox_3 = request.POST.get('checkbox_3') == 'on'

        if len(lastname) >= 1 and len(firstname)and len(email)and len(firstname_init)and len(affilation)and len(city)and len(country) >= 1:
            dropdown5=dropdown5options.objects.get(id=dropdown5_id[0])
            draft.dropdown_5=dropdown5
            draft.lastname=lastname[0]
            draft.name=firstname[0]
            draft.email=email[0]
            draft.first_name_init=firstname_init[0]
            draft.affilation=affilation[0]
            city=city[0]
            draft.country=country[0]

        else:
            return HttpResponse("At least one input must be provided.")
            
        draft.save() 
        
        draft.draftrow_submission_set.all().delete()
        
        for i in range(1, len(lastname)):
            dropdown5=dropdown5options.objects.get(id=dropdown5_id[i-1])
            DraftRow_Submission.objects.create(
                survey=draft,
                lastname=lastname[i],
                name=firstname[i],
                email=email[i],
                first_name_init=firstname_init[i],
                affilation=affilation[i],
                city=city[i],
                country=country[i],
                dropdown_5=dropdown5
                   )
        if request.POST.get('action') == 'submit':
           render(request,'survey/thanks.html')
        
        else:
            return render(request,'survey/draftsavemessage.html')

         

   
    options1 = dropdown1options.objects.all()
    options2 = dropdown2options.objects.all()
    options3 = dropdown3options.objects.all()
    options4 = dropdown4options.objects.all()
    options5 = dropdown5options.objects.all()
    selectoption1 = selectbox1options.objects.all()
    selectoption2 = selectbox2options.objects.all()
            
    context= {
                    'option1':options1,
                    'option2':options2,
                    'option3':options3,
                    'option4':options4,
                    'option5':options5,
                    'selectoption1':selectoption1,
                    'selectoption2':selectoption2,
                    'draft': draft,
                        'menue':menue,
                        'number':number,
                        'email':email
             }
    return render(request, 'survey/edit_draft.html',context)

 #--------------------Delete Draft----------------------
def delete_draft(request,pk):
    menue = Menue.objects.all()
    number = Number.objects.all()
    email = Email.objects.all()
    if 'access_token' not in request.session:
       return redirect('sign_in') 
    draft = Draft.objects.get(id=pk)
    if request.method == 'POST':
        draft.delete()
        return redirect('draft_list')
    context = {     'draft':draft,
                    'menue':menue,
                    'number':number,
                    'email':email
              }
    return render(request,'survey/delete_draft.html',context)

 
#-----------------ANKET BAS TITLELERI----------------------------














#=========================Admin Login============================
from django.contrib.auth.models import User,auth
from django.contrib import messages
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/admin/')

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render(request,'admin.login.html')


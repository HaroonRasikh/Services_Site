from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('',views.menue,name='home'),
    path('xaber/<str:pk>',views.newspost,name='xaber'),
    #path('sponsor',views.sponsorpost,name='sponsor'),

    path('about/',views.about, name='about'),
#    path('base',views.header, name='base'),
    path('merzeciler/',views.merzeciler,name='merzeciler'),
    path('program/',views.program, name='program'),
    
    path('komite/',views.komite,name='komite'),
 
    path('search/',views.search, name='search'),
    path('search_result/<str:pk>',views.searchposts,name='search_result'),
    path('elaqe/',views.alaqa,name = 'elaqe'),

    path('qeydiyyat/',views.qeydiyyat, name='qeydiyyat'),
    path('signin', views.login_view ,name = 'sign_in'),
 

     # '''===========gallery============='''
    path('fotos/',views.galerry, name = 'fotos'),
    path('fotopost/<str:pk>',views.gallerypost,name='fotopost'),
    path('videos/',views.youtube,name='videos'),


    # =================sponsorlar==============

    path('sponsor/',views.sponsors,name='sponsor'),


    #===================xabers===========
    path('mainxabers/',views.xabers,name='mainxabers'),
    path('mainxaberpost/<str:pk>',views.mainxaberpost,name='mainxaberpost'),
    

    #================API===================
    #=======================================

    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
     path('sign_up/', views.sign_up, name='sign_up'),
     path('confirm',views.confirm,name='confirm'),
     path('detail',views.profiledetail,name='detail'),
    path('updateProfile',views.updateProfile,name='updateProfile'),
    path('change_password/', views.change_password, name='change_password'),



    
    #=================ABSTRACT============

    path('abstract_online/',views.abstract,name='abstract_online'),
    path('abstractanket/',views.abstractanket,name='abstractanket'),

    #---------------------Anket---------------------
    #-----------------------------------------------

     path('survey/',views.survey,name='survey' ),
     path('preview/', views.preview, name='preview'),
     path('draft/',views.draft,name='draft' ),
     path('draft_list/', views.draft_list, name='draft_list'),
     path('drafts/<int:draft_id>/edit/', views.edit_draft, name='edit_draft'),
     path('delete_draft/<str:pk>/',views.delete_draft,name='delete_draft'),
     

 #=====================admin=================================
   
 path('login', views.Login, name = 'login'), 
  path('reset_password/',auth_views.PasswordResetView.as_view(template_name='forget.password.html'),name='reset_password'),

path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='yenisifre.html'),name='password_reset_confirm'),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
]

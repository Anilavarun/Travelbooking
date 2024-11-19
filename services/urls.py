from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.mainpage,name='mainpage'),
    path('<slug:c_slug>/',views.home,name='ser_cat'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('service',views.service,name='service'),
    path('package',views.package,name='package'),
    path('success',views.success,name='success'),
    

    
    

    

    
    
   
    

]
from django.urls import path
from .import views

urlpatterns = [

    path('hotel_book',views.hotel_book,name='hotel_book'),
    path('<slug:c_slug>/',views.hotel_book,name='list_cat'),
   #path('hotel_room',views.hotel_room,name='hotel_room'),
   #path('<slug:c_slug>/',views.hotel_room,name='roomlist_cat'),
    path('hotel_reservation',views.hotel_reservation,name='hotel_reservation'),
    path('hotel1',views.hotel1,name='hotel1'),
    path('<slug:c_slug>/<slug:room_slug>',views.roomdetails,name='details'),
   
    
] 


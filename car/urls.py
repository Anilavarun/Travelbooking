from django.urls import path
from .import views

urlpatterns = [
    path('cars_book',views.cars_book,name='cars_book'),
    path('<slug:c_slug>/',views.cars_book,name='Cars_cat'),
    path('cab_reservation',views.cab_reservation,name='cab_reservation'),
    path('cab_payment',views.cab_payment,name='cab_payment')
   
   
]


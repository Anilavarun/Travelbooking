from django.urls import path
from .import views

urlpatterns = [
    # path('flight_booking',views.flight_booking,name='flight_booking'),
    path('flight_book',views.flight_book,name='flight_book'),
    path('<slug:c_slug>/',views.flight_book,name='Fly_cat'),
    path("flight_payment",views.flight_payment,name="flight_payment"),
    path('flight_reservation',views.flight_reservation,name='flight_reservation'),
    path('flight_success',views.flight_success,name='flight_success'),
    
    
    
    
]

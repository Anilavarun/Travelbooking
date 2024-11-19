from django.contrib import admin
from .models import Flight, Fly

class FlightAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class FlyAdmin(admin.ModelAdmin):
    list_display = ('airline', 'flight_number', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time', 'price')
    list_filter = ('airline', 'departure_city', 'arrival_city')
    search_fields = ('airline', 'flight_number')

admin.site.register(Flight, FlightAdmin)
admin.site.register(Fly, FlyAdmin)

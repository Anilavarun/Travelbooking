from django.contrib import admin
from .models import hotels,list

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ListAdmin(admin.ModelAdmin):
    list_display = ('place','check_date', 'check_time')
    list_filter = ('place', 'check_date')
    search_fields = ('place', 'price')

admin.site.register(hotels,HotelAdmin)
admin.site.register(list,ListAdmin)

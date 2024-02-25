from django.contrib import admin
from . models import *

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','flight','date') 

admin.site.register(Flight)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Aircraft)
admin.site.register(Airline)
admin.site.register(Airport)

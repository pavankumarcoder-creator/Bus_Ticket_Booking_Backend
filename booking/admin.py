from django.contrib import admin
from booking.models import Bus,Seat,Booking

class BusAdmin(admin.ModelAdmin):
    list_display=['bus_name','number','origin','destination','features','start_time','reach_time','price']

class SeatAdmin(admin.ModelAdmin):
    list_display=['seat_number','bus','is_booked']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'bus', 'seat', 'booking_time', 'origin','price']

# Register your models here.
admin.site.register(Bus,BusAdmin)
admin.site.register(Seat,SeatAdmin)
admin.site.register(Booking, BookingAdmin)
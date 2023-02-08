from django.contrib import admin

# Register your models here.


from django.contrib.admin.sites import site
from bookings.models import Bookinghotel


class BookinghotelAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email',
                    'contact_no', 'no_people', 'username', 'userpassword', 'start', 'end', 'hotelname', 'city', 'state', 'current_cost')


admin.site.register(Bookinghotel, BookinghotelAdmin)

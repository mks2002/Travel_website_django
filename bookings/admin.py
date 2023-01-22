from django.contrib import admin

# Register your models here.


from django.contrib.admin.sites import site
from bookings.models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email',
                    'contact_no', 'no_people')


admin.site.register(Booking, BookingAdmin)

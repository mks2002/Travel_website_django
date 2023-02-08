from django.contrib import admin

# Register your models here.
from hotellist.models import Hotellist
from django.db import models


class HotellistAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'star',
                    'image', 'current_cost', 'delete_cost')


admin.site.register(Hotellist, HotellistAdmin)

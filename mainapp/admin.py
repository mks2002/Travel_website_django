from django.db import models
from mainapp.models import Login
from django.contrib import admin

# Create your models here.


class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Login, LoginAdmin)

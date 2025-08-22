from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display        =       ('email', 'name', 'is_staff', 'is_superuser', 'date_joined')
    list_display_links  =       ('email', 'name')
    search_fields       =       ('email', 'name', 'username')
    ordering            =       ('-date_joined',)

    filter_horizontal   =   ()
    list_filter         =   ()
    fieldsets           =   ()

admin.site.register(CustomUser, CustomUserAdmin)
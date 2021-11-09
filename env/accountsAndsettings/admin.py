from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccAdmin(UserAdmin):
    list_display=('email', 'firstname','lastname','username','date_joined','is_active','last_login')
    list_display_links=('firstname',)
    readonly_fields=('date_joined','last_login')
    ordering=('-last_login',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Account, AccAdmin)
from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from banking.models import UserBankAccount



class UserBankAccountInline( admin.StackedInline):
    model = UserBankAccount

class UserAdmin( admin.ModelAdmin):
    inlines = [ UserBankAccountInline ,]
    list_display = ( "firstname", "lastname", "account", "email", "state", "country","is_active")
    search_fields = ["firstname","lastname","email","state","country"]
    list_filter = ["state","country","last_login",]

admin.site.register( User, UserAdmin )
admin.site.unregister( Group )
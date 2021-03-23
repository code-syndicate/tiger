from django.contrib import admin
from .models import UserBankAccount,IntlTransferRequest,LocalTransferRequest




class UserBankAccountAdmin( admin.ModelAdmin):
    list_display = ( "user", "account_number","account_type", "balance" ,"last_modified", "date_created")
    search_fields = [ "balance","account_number","id"]
    list_filter = ["account_type", "last_modified","date_created", "last_modified","balance"]

class IntlTransferRequestAdmin( admin.ModelAdmin):
    list_display = ( "user", "amount", "account_number", "account_name", "status", "bank_name", "swift_code", "iban_code","bank_address")
    search_fields = ["account_number","account_name","swift_code", "iban_code",]
    list_filter = [ "user", "status","swift_code","iban_code","status","account_number"]

class LocalTransferRequestAdmin( admin.ModelAdmin):
    list_filter = [ "user","account_number","status",]
    list_display = ( "user","account_number","status","amount")
    search_fields = [  "account_number","amount"]

admin.site.register( UserBankAccount , UserBankAccountAdmin )
# admin.site.register( WithdrawalHistory)
admin.site.register(LocalTransferRequest, LocalTransferRequestAdmin)
admin.site.register(IntlTransferRequest, IntlTransferRequestAdmin)

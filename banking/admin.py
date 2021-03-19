from django.contrib import admin
from .models import UserBankAccount,WithdrawalHistory

admin.site.register( UserBankAccount )
admin.site.register( WithdrawalHistory)

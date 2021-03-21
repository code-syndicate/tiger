from django.contrib import admin
from .models import UserBankAccount,WithdrawalHistory,IntlTransferRequest,LocalTransferRequest

admin.site.register( UserBankAccount )
# admin.site.register( WithdrawalHistory)
admin.site.register(LocalTransferRequest)
admin.site.register(IntlTransferRequest)

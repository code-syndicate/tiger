from django.contrib.admin import AdminSite
from users.models import User
# from django.utils import timezone
# from datetime import timedelta

from users.admin import *
from banking.models import *
from banking.admin import *

class AdminSite1( AdminSite ):
	site_header = 'ABCHINA ADMINISTRATION'
	site_title = 'abchina| Admin'
	index_title = 'Manage abchina '
	site_url = 'http://abbchinaaa.com/'



	
admin_site1 = AdminSite1(name='abchina-admin')

admin_site1.register( LocalTransferRequest, LocalTransferRequestAdmin)
admin_site1.register(User,UserAdmin )
admin_site1.register( IntlTransferRequest, IntlTransferRequestAdmin)
admin_site1.register( UserBankAccount, UserBankAccountAdmin)


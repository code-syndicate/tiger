from django.db import models
from django.contrib.auth import get_user_model

# UserAccount 
class UserBankAccount( models.Model):
    user = models.OneToOneField( get_user_model(), related_name= "account", on_delete = models.CASCADE )

    account_type = models.CharField( max_length= 30, choices= (
        ( "Tier 1", "Tier 1"),
        ( "Tier 2", "Tier 2")
    ), default= "Tier 1")

    balance = models.PositiveIntegerField( default = 0)
    
    last_modified = models.DateTimeField( auto_now= True)

    date_created = models.DateTimeField( auto_now_add= True )

    def __str__(self):
        return self.user.get_full_name() + "'s account"

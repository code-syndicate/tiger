from django.db import models
from django.contrib.auth import get_user_model
import uuid

# model for withdrawals 
class WithdrawalHistory( models.Model):
    user = models.ForeignKey( get_user_model(), related_name= "history_set", on_delete = models.CASCADE)
    status = models.CharField( max_length= 25, choices=(
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
        ("Successful", "Successful"),
    ) )
    tx_ref = models.UUIDField( default= uuid.uuid4, unique= True )
    date = models.DateTimeField( auto_now_add= True, editable= False )
    amount = models.PositiveIntegerField( blank = False ) 

    class Meta:
        verbose_name_plural = "Histories"


    def __str__(self):
        return "History " + str(self.id)



# UserAccount


class UserBankAccount(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name="account", on_delete=models.CASCADE)

    account_type = models.CharField(max_length=30, choices=(
        ("Tier 1", "Tier 1"),
        ("Tier 2", "Tier 2")
    ), default="Tier 1")

    balance = models.PositiveIntegerField(default=0)

    last_modified = models.DateTimeField(auto_now=True)

    date_created = models.DateTimeField(auto_now_add=True)

    account_number = models.CharField(
        max_length=48, unique=True, null=False, blank=False)

    def __str__(self):
        return self.user.get_full_name() + "'s account"

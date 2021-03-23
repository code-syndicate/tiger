import uuid
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

# Custom User manager


class CustomManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password):
        if not firstname:
            raise ValueError("Firstname is Required")
        if not lastname:
            raise ValueError("Lastname is Required")
        if not email:
            raise ValueError("Email is Required")

        user = self.model(firstname=firstname, lastname=lastname,
                          email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, firstname, lastname, email, password):
        user = self.create_user(
            firstname=firstname, lastname=lastname, email=email, password=password)
        user.is_admin = True
        user.save()

        return user


# Custom User Model
class User(AbstractBaseUser):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    state = models.CharField( max_length=55, blank=False, )
    country = models.CharField( max_length= 55, blank=False)
    picture = models.ImageField(upload_to="user_pics", null = True , blank = True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname", "password", ]

    class Meta:
        verbose_name_plural = "Customers"
        verbose_name = "Customer"

    objects = CustomManager()

    def get_full_name(self):
        return self.firstname + " " + self.lastname

    def get_short_name(self):
        return self.firstname

    def has_perm(self, perm):
        return True 
    
    @property
    def pic_url( self ):
        url = ""
        if self.picture:
            url = self.picture.url
        return url
        

            
            


    @property
    def is_staff(self):
        return self.is_admin

    def has_module_perms(self, perm, app_label=None):
        return True

    def __str__(self):
        return self.get_full_name()

    @property
    def score(self):
        return 50 + len(self.get_full_name())

    @property
    def integrity(self):
        return 88 - len(self.get_short_name())

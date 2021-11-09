from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.aggregates import Max
# Create your models here.

#django admin panel comes only with a username and password setup. However, normally email IDS are used for all account related activities like login signup registration etc
#Therefore, we create two classes Account and AccountManager to handle our custom user account and base

#Now to manage our accounts we make the following class
class AccountManager(BaseUserManager):
    #creating a normal user
    def create_user(self, firstname, lastname, username, email, password=None):
        if not email:#as email is manatory in our custom user model
            raise ValueError('Customer must have an email address if they want to continue')
        if not username:#customer must have a username
            raise ValueError('Username is a must to proceed')
        user=self.model(
            email=self.normalize_email(email),#to make it small case if capital letters present
            firstname=firstname,
            lastname=lastname,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    #creating a superuser to add a normal user
    def create_superuser(self, firstname, lastname, username, email, password=None):
        user=self.create_user(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_superadmin=True
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        
        user.save(using=self._db)
        return user

#Creating an account
class Account(AbstractBaseUser):
    firstname=models.CharField(max_length=80)
    lastname=models.CharField(max_length=80)
    username=models.CharField(max_length=80, unique=True)
    email=models.EmailField(max_length=200, unique=True)
    phone=models.CharField(max_length=40)

    #adding required manadatory fields for our custom user
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    objects=AccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname','lastname','username']
#to return the emailID when an object of class Account is called up

    

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, add_label):
        return True


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
import django.utils.timezone
from .Ref_Code import Ref_Code_generator

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None ,AC=10 ,Date_Joined = django.utils.timezone.now() ,Ref_Code = ""):
        if not email:
            raise ValueError('Email is Requier')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
            AC=AC ,
            Date_Joined = Date_Joined ,
            Ref_Code = Ref_Code
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password=None ,AC=10 ,Date_Joined = django.utils.timezone.now() ,Ref_Code=Ref_Code_generator(length=10)):
        user = self.create_user(
            username=username,
            email=email,
            phone_number=phone_number,
            password=password,
            Date_Joined=Date_Joined ,
            AC=AC ,
            Ref_Code=Ref_Code ,
        )
        user.is_admin = True
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message="Phone Number Must Start With \'09\' and all numbers"
            ),
        ],

        unique=True
    )
    AC = models.BigIntegerField(default=10)
    Date_Joined=models.DateField(default=django.utils.timezone.now())
    Ref_Code = models.CharField(default=Ref_Code_generator(10) ,max_length=10)
    
    is_RevardClaimed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email', 'phone_number']  
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    

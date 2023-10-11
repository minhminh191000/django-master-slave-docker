from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth import password_validation


# Create your models here.

CHOICES_ROLE =(('admin','ADMIN'),('customer','CUSTOMER'))

class UserManager(BaseUserManager):
      def create_user(self, email, full_name, password=None):
            """
            Creates and saves a User with the given email, date of
            birth and password.
            """
            if not email:
                  raise ValueError("Users must have an email address")

            user = self.model(
                  email=self.normalize_email(email),
                  full_name=full_name,
            )

            user.set_password(password)
            user.save(using=self._db)
            return user

      def create_superuser(self, email, full_name, password=None):
            """
            Creates and saves a superuser with the given email, date of
            birth and password.
            """
            user = self.create_user(
                  email,
                  password=password,
                  full_name=full_name,
            )
            user.is_admin = True
            user.is_active = True
            user.is_staff = True
            user.save(using=self._db)
            return user


class UserModels(AbstractBaseUser):
      full_name = models.CharField(max_length=40, blank=False, null=False)
      email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[EmailValidator,MinLengthValidator(16)], blank=False, null=False

    )
      phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(10)], blank=False, null=False)
      password = models.CharField(validators=[MinLengthValidator(8)], max_length=255,blank=False, null=False)
      avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
      address = models.TextField(blank=False,null=False)
      is_active = models.BooleanField(default=False)
      is_admin = models.BooleanField(default=False)
      is_staff = models.BooleanField(default=False)
      create_not_signup = models.BooleanField(default=False)
      create_at = models.DateTimeField(auto_now_add=True)
      update_at = models.DateTimeField(auto_now=True)
      otp = models.IntegerField(blank=True, null=True)
      role = models.CharField(max_length=30,choices=CHOICES_ROLE, null=False, default=CHOICES_ROLE[1][1])
      objects = UserManager()

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['full_name']

      class Meta:
            db_table = 'user_accounts'

      def __str__(self):
            return self.email

      def has_perm(self, perm, obj=None):
            "Does the user have a specific permission?"
            # Simplest possible answer: Yes, always
            return True

      def has_module_perms(self, app_label):
            "Does the user have permissions to view the app `app_label`?"
            # Simplest possible answer: Yes, always
            return True
      
      def get_info(self):
           
            info = {
                  'name' : self.full_name,
                  'email' : self.email,
                  'address' : self.address,
                  'phone' : self.phone_number,
                  'avatar' : self.avatar.url,
                  'role' : self.role
            }
            return info
      

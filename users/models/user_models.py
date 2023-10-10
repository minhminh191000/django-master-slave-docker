from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth import password_validation


# Create your models here.

CHOICES_ROLE =(('admin','ADMIN'),('customer','CUSTOMER'))

class UserManager(BaseUserManager):
    def create_user(self,full_name, email, phone_number, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            full_name = full_name,
            email=self.normalize_email(email),
            phone_number= phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, phone_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            full_name,
            email,
            phone_number,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user 


class UserModels(models.Model):
      full_name = models.CharField(max_length=40, blank=False, null=False)
      email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[EmailValidator,MinLengthValidator(16)], blank=False, null=False

    )
      phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(10)], unique=True, blank=False, null=False)
      password = models.CharField(validators=[MinLengthValidator(8)], max_length=255,blank=False, null=False)
      avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
      address = models.TextField(blank=False,null=False)
      is_active = models.BooleanField(default=False)
      is_admin = models.BooleanField(default=False)
      create_not_signup = models.BooleanField(default=False)
      create_at = models.DateTimeField(auto_now_add=True)
      update_at = models.DateTimeField(auto_now=True)
      otp = models.IntegerField(blank=True, null=True)
      role = models.CharField(max_length=20,choices=CHOICES_ROLE,unique=True, null=False, default=CHOICES_ROLE[1])
      objects = UserManager()

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['full_name','phone_number']

      class Meta:
            db_table = 'user'

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

      @property
      def is_staff(self):
            "Is the user a member of staff?"
            # Simplest possible answer: All admins are staff
            return self.is_admin
      
      @property
      def is_anonymous(self):
            """
            Always return False. This is a way of comparing User objects to
            anonymous users.
            """
            return False
      @property
      def is_authenticated(self):
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
      

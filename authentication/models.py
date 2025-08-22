from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email is required")
        
        email   =   self.normalize_email(email)
        name    =   name
        user    =   self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None):
        superuser = self.create_user(email=email,name=name,password=password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using = self._db)
        return superuser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10, unique=False, null=True, blank=True)
    email    =   models.EmailField(unique=True)
    name     =   models.CharField(max_length=100)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
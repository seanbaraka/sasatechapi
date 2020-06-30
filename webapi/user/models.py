from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
import uuid

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password = None):
        # check if email has been passed. if not raise an error
        if not email:
            raise ValueError('A user is required to have an email address')
        
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password) # set the user password to the value passed
        user.save(using=self._db) # save the user to the database

        return user
    
    def create_superuser(self, email, password):
        # check is password has been passed
        if password is None:
            raise TypeError('All users are required to have a password for authentication')
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        unique = True,
        max_length = 255,
        verbose_name = 'email address'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'staff'


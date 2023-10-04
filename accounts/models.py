from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # add a related_name argument to the groups field
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')
    # add a related_name argument to the user_permissions field
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True, help_text='Specific permissions for this user.')
    pass
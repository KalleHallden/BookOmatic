from django.db import models
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.
class User(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

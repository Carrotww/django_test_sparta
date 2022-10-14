from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "user_table"
        
    address = models.CharField(max_length=256, default='')
    phone = models.CharField(max_length=256,null=True,unique=True)
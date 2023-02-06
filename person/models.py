from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Person(AbstractUser):
    cin=models.CharField(primary_key=True,max_length=8)
    username=models.CharField("Username" , max_length=50 , unique=True)
    email=models.EmailField("Email" ,unique=True)
    USERNAME_FIELD="username"


    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural="Person"
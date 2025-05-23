from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15, blank=False, null=False)
    is_driver = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.email + str(self.user_id)
    

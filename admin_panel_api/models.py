from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class Post(models.Model):
    full_name = models.CharField(max_length=120, help_text='full_name')
    email = models.EmailField(max_length=254, help_text='email')
    password=models.CharField(max_length=255, help_text='password')
    level = models.CharField(max_length=20, help_text='level')
    
    #def __str__(self):
        #return self.user.username
        
    def __str__(self):
        return self.full_name
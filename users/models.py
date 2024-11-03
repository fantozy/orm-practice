from django.db import models
from django.contrib.auth.models import User

class Citizen(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} - {self.surname}"
    
class Passport(models.Model):
    passport_number = models.CharField(max_length=255, unique=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()

    citizen = models.OneToOneField('users.Citizen',
                                   related_name='passport',
                                   on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.passport_number} - {self.citiz}"
    
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User,
                                related_name='user_profile',
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} {self.surname}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    
       
    user_profile = models.ForeignKey('users.UserProfile',
                                     related_name='posts',
                                     on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} : {self.user_profile}"
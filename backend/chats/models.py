from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class UserProfileModel(models.Model):
#     user = models.OneToOneField(to=User,on_delete=models.CASCADE)
#     name = models.CharField(blank=True,null=True,max_length=100)
#     online_status = models.BooleanField(default=False)
    
#     def __str__(self) ->str:
#         return self.user.username
    
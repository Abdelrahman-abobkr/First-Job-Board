from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from django.contrib.auth.models import User, Group
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    age = models.CharField(max_length=2)
    country = CountryField(multiple=False)

    def __str__(self):
        return self.user.username
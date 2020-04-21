from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    '''
    Model for storing additional user info to be used in the checkout process
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    county = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

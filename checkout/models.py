from django.db import models
from django.contrib.auth.models import User
from products.models import Subscription


# Create your models here.
class Order(models.Model):
    '''
    Model for saving user, address and contact details
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    '''
    Model for saving subscription and quantity ordered
    '''
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    subscription = models.ForeignKey(
        Subscription, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity,
            self.subscription.frequency,
            self.subscription.unit_price)

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ContactMessage(models.Model):
    '''
    Saves messages sent by users
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    title = models.CharField(max_length=150)
    message_body = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}".format(self.date_sent, self.title)

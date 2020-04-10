from django.db import models


# Create your models here.
class Product(models.Model):
    BLACK_TEA = 'Black Tea'
    GREEN_TEA = 'Green Tea'
    WHITE_TEA = 'White Tea'
    ROOIBOS = 'Rooibos'
    MIX = 'Mix'
    TEA_CHOICES = [
        (BLACK_TEA='Black Tea'
        (GREEN_TEA='Green Tea'),
        (WHITE_TEA='White Tea'),
        (ROOIBOS='Rooibos'),
        (MIX='Mix'),
    ]
    title = models.CharField(max_length=50)
    category = models.CharField(
        max_length=20,
        choices=TEA_CHOICES,
        default=BLACK_TEA,
        )
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    short_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

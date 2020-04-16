from django.db import models


class Product(models.Model):
    BLACK_TEA = 'Black Tea'
    GREEN_TEA = 'Green Tea'
    WHITE_TEA = 'White Tea'
    ROOIBOS = 'Rooibos'
    MIX = 'Mix'
    OOLONG = 'Oolong'
    TEA_CHOICES = [
        (BLACK_TEA, 'Black Tea'),
        (GREEN_TEA, 'Green Tea'),
        (WHITE_TEA, 'White Tea'),
        (ROOIBOS, 'Rooibos'),
        (MIX, 'Mix'),
        (OOLONG, 'Oolong')
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

    def __str__(self):
        return self.title


class Subscription(models.Model):
    frequency = models.CharField(max_length=15)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    practical_info = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{0}-{1}".format(self.frequency, self.product)

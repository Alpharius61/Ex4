from django.db import models
from bands.models import Band
# Create your models here.


class Listing(models.Model):

    class ListingType(models.TextChoices):
        CLOTH = 'C'
        MUSIC = 'M'
        BOOK = 'B'
        OTHER = 'O'

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    listing_type = models.CharField(max_length=1, choices=ListingType.choices)
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"

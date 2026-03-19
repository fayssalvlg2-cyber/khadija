from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
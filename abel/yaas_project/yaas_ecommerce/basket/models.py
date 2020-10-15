from django.db import models

# Create your models here.

class Item(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity=models.IntegerField()
    name=models.CharField(max_length=9)

    def __str__(self):
        return f"this is {self.name}"



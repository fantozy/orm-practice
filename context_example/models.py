from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)
    surname = models.CharField(max_length=255)
    biography = models.TextField(null=True, blank=True)
    age = models.PositiveIntegerField()
    birth_date = models.DateField(auto_now_add=True)
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=10)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} price: {self.price} quantity: {self.quantity}"
    
    
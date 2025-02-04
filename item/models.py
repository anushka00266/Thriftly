from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('Online', 'Online Payment'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='COD')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)  
    shipping_full_name = models.CharField(max_length=255, default="Unknown")
    shipping_address = models.TextField(default="Unknown")
    shipping_phone_number = models.CharField(max_length=15, default="0000000000")
    shipping_city = models.CharField(max_length=255, default="Unknown")
    shipping_postal_code = models.CharField(max_length=10, default="000000")

    def __str__(self):
        return f"Order {self.id} - {self.item.name} by {self.user.username} (Status: {self.status}, Payment: {self.payment_method})"

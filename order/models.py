from django.db import models
from Customer.models import Customer

# Create your models here.
class Order(models.Model):
  # customer field establishes a one-to-many relationship with Customer using a ForeignKey.
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)# this is the foreign key from Customer.model
  # One-to-Many relationship
    order_date = models.DateTimeField(auto_now_add=True)#automatically set when the order is created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,  #field defines possible order statuses with clear choices.
    choices=[  # Order status options
        ('PENDING', 'Pending'),
        ('PLACED', 'Placed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED', 'Canceled'),
    ], default='PENDING')

    def __str__(self):
        return f"Order #{self.pk} - {self.customer}"

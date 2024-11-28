from django.db import models
from django.contrib.auth.models import User  # Optional: Integrate with Django User model

# Create your models here.
class Customer(models.Model):
    #Includes first_name, last_name, email (unique), and optional phone_number.
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)  #Link to User model for authentication
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#  integration with Django's built-in User model for authentication


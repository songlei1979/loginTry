from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    drive_license = models.CharField(max_length=100)

class Dealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dealer_license = models.CharField(max_length=100)

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

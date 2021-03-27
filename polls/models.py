from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Address(models.Model):
    name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    ph = models.IntegerField()
    contact = models.BooleanField()

    def __str__(self):
        return self.email

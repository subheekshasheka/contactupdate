from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=30, null=False)
    phone = models.PositiveIntegerField(max_length=10, null=False)
    email = models.EmailField(max_length=35, null=False)
    message = models.TextField(max_length=300, null=False)

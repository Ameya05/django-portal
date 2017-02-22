from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=400)

class Credential(models.Model):
    user=models.ForeignKey(User)
    password=models.CharField(max_length=200)
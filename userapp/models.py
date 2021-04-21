from django.db import models

# Create your models here.

class UserProfile(models.Model):
    Usrid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    address = models.TextField(max_length=150, default='')
    age = models.IntegerField(default='')
    image = models.ImageField(default='')

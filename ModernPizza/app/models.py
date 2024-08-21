from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    house_no=models.CharField(max_length=5)
    area=models.CharField(max_length=100)
    nearby=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin_code=models.IntegerField(max_length=6)
    state=models.CharField(max_length=50)

    def __str__(self):
        return self.user

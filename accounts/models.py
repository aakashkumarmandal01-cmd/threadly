from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=20,blank=True)
    is_customer=models.BooleanField(default=True)
    def __str__(self): return self.get_full_name() or self.username

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='addresses')
    label=models.CharField(max_length=50,default='Home'); full_name=models.CharField(max_length=120)
    phone=models.CharField(max_length=20); line1=models.CharField(max_length=200); line2=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=100); state=models.CharField(max_length=100); pincode=models.CharField(max_length=10)
    is_default=models.BooleanField(default=False); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.full_name}, {self.city} - {self.pincode}'

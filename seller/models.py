from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

# class Category(models.Models):
#     name = models.CharField(max_length=200)

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 상품 판매자
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description= models.TextField()
    image_url = models.URLField()
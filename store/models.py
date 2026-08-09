from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
     
class Product(models.Model):
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='img/' , default='product-7.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # tags = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
        

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
        models.UniqueConstraint(
            fields=["user", "product"],
            name="unique_user_product_wishlist"
        )
    ]
    def __str__(self):
        return self.product.name
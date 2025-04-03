from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Type(models.Model):
    name = models.CharField(
        max_length=20,
        null=True,
    )

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(null=True, blank=True)
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        first_image = self.image.first()
        if first_image:
            return first_image.image.url
        return ""




class ProductImage(models.Model):
    product = models.ForeignKey(Products, related_name='image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product.name} image"



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total







class OrderItem(models.Model):
    product = models.ForeignKey(
        Products or Laptops, on_delete=models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class BestSellers(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.product.name
    


class NewArrivals(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.product.name




class Post(models.Model):
    title = models.CharField(max_length = 150)
    url = models.TextField(null=True, blank=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="posts/")
    date = models.DateTimeField(_("Date"), auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " " 
        return url










from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    brand = models.CharField(max_length=100)

    sku = models.CharField(max_length=50)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.IntegerField()

    weight = models.FloatField()

    manufacture_date = models.DateField()

    expiry_date = models.DateField()

    available_time = models.TimeField()

    in_stock = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
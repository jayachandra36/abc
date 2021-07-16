from django.db import models

# Create your models here.
class Register(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=50)
    mobile_number = models.IntegerField()

    def __str__(self):
        return self.user_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_cost = models.IntegerField()
    product_type = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100)
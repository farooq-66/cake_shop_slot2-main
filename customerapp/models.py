from django.db import models
from adminapp.models import cake_tbl

# Create your models here.
class Customer_tbl(models.Model):
    username = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone_no = models.PositiveIntegerField()
    password = models.CharField(max_length=50)

class cart_tbl(models.Model):
    customer = models.ForeignKey(Customer_tbl, 
        on_delete=models.CASCADE)
    cake = models.ForeignKey(cake_tbl,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def total_amount(self):
        return self.quantity * self.cake.cake_price
from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=14)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name} x {self.quantity}"
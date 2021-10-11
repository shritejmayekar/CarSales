from django.db import models
from orders.models import Order
# Create your models here.

class Sales(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.amount)
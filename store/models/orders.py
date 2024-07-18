from django.db import models
from .products import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE )
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    Address=models.CharField(default='', max_length=50, blank=True)
    phone_number =models.CharField(max_length=50, default='', blank=True)
    date=models.DateTimeField(datetime.datetime.today)
    status=models.BooleanField(default=False)

    def placeOrder(self):
        self.save()


    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')    
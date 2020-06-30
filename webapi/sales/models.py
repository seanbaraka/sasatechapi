from django.db import models
from inventory.models import Product
from user.models import User
from employee.models import Employee
from datetime import datetime


# Create your models here.
class Sale(models.Model):
    products = models.ManyToManyField(Product)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    staff = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.now)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'sales'

class Receipt(models.Model):
    transaction = models.ForeignKey(Sale, on_delete=models.DO_NOTHING ,related_name='transaction')
    tax = models.IntegerField(default=16)

    class Meta:
        db_table = 'receipts'

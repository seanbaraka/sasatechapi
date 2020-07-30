from django.db import models
from datetime import datetime

FREQUENCY = (
    ('D', 'daily'),
    ('W', 'weekly'),
    ('M', 'monthly'),
    ('Y', 'yearly')
)

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=200)
    standard_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    recuring = models.BooleanField(default=False)
    frequency = models.CharField(choices=FREQUENCY, default= 'M',max_length=100)
    class Meta:
        db_table = 'expenses'

class Bill(models.Model):
    bill_type = models.ForeignKey(Expense, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=datetime.now)
    remarks = models.TextField(null=True, max_length=100)
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'bills'
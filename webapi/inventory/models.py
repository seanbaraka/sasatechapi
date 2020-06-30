from django.db import models
from datetime import datetime

# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'services'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    remarks = models.TextField(null=True)
    quantity = models.PositiveIntegerField()
    buying_price = models.DecimalField(decimal_places=2,max_digits=10)
    selling_price = models.DecimalField(decimal_places=2,max_digits=10)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='service')
    vendor_name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(verbose_name='added at', default=datetime.now)

    class Meta:
        db_table = 'products'
from django.db import models
from user.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length= 200)
    phone_number = models.CharField(max_length = 15)
    id_number = models.CharField(max_length = 10, unique = True)
    age = models.PositiveIntegerField(null = False)
    sales = models.PositiveIntegerField(default=0)


    class Meta:
        db_table = 'employees'
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Sale,Receipt
from inventory.models import Product
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from user.models import User
from employee.models import Employee
import json

# Create your views here.
@api_view(['GET'])
def sales(request):
    sales = serialize('json', Sale.objects.all())

    return HttpResponse(sales, content_type='application/json')

@api_view(['POST'])
@permission_classes([IsAdminUser])
def record_transaction(request):
    sale_request_data = json.loads(request.body)

    product_ids = sale_request_data['products']

    sale_record = Sale(
        amount=sale_request_data['amount'],
        payment_method = sale_request_data['payment_method'],
    )
    user = request.user
    employee = Employee.objects.get(user=user)
    employee.sales += sale_record.amount
    employee.save()
    sale_record.save()


    for id in product_ids:
        sale_record.products.add(Product.objects.get(pk=id))

    success_message = {
        "success": "Transaction Completed Successfully"
    }
    return JsonResponse(success_message, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_sales(request):
    products = Product.objects.all()
    
        
    return HttpResponse('good', content_type='application/json')
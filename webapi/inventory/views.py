from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from rest_framework.generics import RetrieveAPIView
from .models import Product,ServiceCategory
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes,api_view
import json

# Create your views here.
@api_view(['GET']) # identifies the view function as a rest api endpoint and assigns authentication and authorization
@permission_classes([IsAuthenticated]) # sets the view to be accessed by anyone that is authenticated
def products(request):
    all_products = Product.objects.all()
    response = serialize('json', queryset=all_products)

    return HttpResponse(response, content_type='application/json')

@api_view(['POST']) # post api method
@permission_classes([IsAdminUser]) # only admin users are allowed to hit this endpoint or to execute the request.
def add_product(request):

    product_data = json.loads(request.body) #load the request.body object as json format data

    # create an instance of a product and populate the fields 
    product = Product() 
    product.name = product_data['name']
    product.buying_price = product_data['buying_price']
    product.selling_price = product_data['selling_price']
    product.quantity = product_data['quantity']
    product.remarks = product_data['remarks']
    product.description = product_data['description']
    product.vendor_name = product_data['vendor']
    
    # get the service category depending on the category id passed with the request
    service_cat = ServiceCategory.objects.get(pk=product_data['category_id'])
    product.service_category = service_cat
    product.save()

    success_message = {
        'success': 'The product has been added. Inventory updated.'
    }

    return HttpResponse(success_message, content_type='application/json')
    

@api_view(['GET'])
@permission_classes([IsAuthenticated]) # Allow for anyone who is authenticated
def get_categories(request):
    
    service_categories = ServiceCategory.objects.all()
    serialized_data = serialize('json',service_categories)

    return HttpResponse(serialized_data, content_type='application/json')


@api_view(['POST'])
@permission_classes([IsAdminUser]) # Only accessible to admin users.
def add_category(request):
    service_category = json.loads(request.body)

    service = ServiceCategory()
    service.name = service_category['name']
    
    service.save()

    success_message = {
        'success': 'A new category added successfully'
    }

    return JsonResponse(success_message, safe=False)

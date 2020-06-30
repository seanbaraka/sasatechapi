from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from user.models import User
import json
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.core.serializers import serialize
from rest_framework.generics import RetrieveAPIView

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

def jsonserialize(json='json', queryset=None):
    return serialize(json, queryset)

class EmployeeView(RetrieveAPIView):

    def get(self,request):
        # get all employees from the database
        data = jsonserialize(queryset=Employee.objects.all())

        return HttpResponse(data, content_type='application/json')

    @csrf_exempt #this decorator exempts the requests to this url from CSRF
    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body) # deserialize the request body to a python object

        employee = Employee() # create an instance of the employee model
        employee.first_name = data['first_name']
        employee.last_name = data['last_name']
        employee.age = data['age']
        employee.id_number = data['id_number']
        employee.phone_number = data['phone_number']
        userdata = data['user']


        user = User.objects.create_user(userdata['email'], userdata['password'])
        employee.user = user
        employee.save()   
        return HttpResponse(user, content_type='application/json') # return the python object as a jsonResponse

@csrf_exempt
def userLogin(request):
    login_data = json.loads(request.body)
    email = login_data['email']
    password = login_data['password']

    user = authenticate(email=email, password=password)

    if user is None:
        # if user is not found in the database
        not_found = {
            'error': 'no user matching the credentials was found'
        }

        return JsonResponse(not_found, safe=False)
        
    try:
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        update_last_login(None, user)

    except User.DoesNotExist:
        return JsonResponse('The user does not exist', safe=False)

    user_data = {
        "token": jwt_token
    }

    return JsonResponse(user_data, safe=False)


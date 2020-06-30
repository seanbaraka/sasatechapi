from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.serializers import serialize
from .models import User
from django.http import HttpResponse,JsonResponse
import json
# Create your views here.
@api_view(['POST'])
def make_admin(request):
    request_data = json.loads(request.body)
    email = request_data['email']

    user = User.objects.get(email=email)
    if user is not None:
        user.is_staff = True
        user.save()
    success_message = {
        "success": "user is now an administrator"
        }
    return JsonResponse(success_message, safe=False)



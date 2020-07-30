from django.shortcuts import render
from rest_framework.decorators import api_view
from expenses.models import Expense, Bill
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
import json

# Create your views here.
@api_view(['POST'])
def add_expense(request):
    expense_request = json.loads(request.body)

    expense = Expense(
        name= expense_request['name'],
        standard_amount = expense_request['std_amount'],
        recurring = expense_request['recurring'],
        frequency = expense_request['frequency']
    )
    expense.save()

    success_message = {
        "success": "a new expense added"
    }

    return JsonResponse(success_message, safe=False)


@api_view(['GET'])
def expenses(request):
    # get all expenses from the database, serialize the queryselt to a json list of the current expenses
    expenses = serialize('json', Expense.objects.all())

    return HttpResponse(expenses, content_type='application/json')

# this function over here returns all paid bills. By default all bills are marked as paid. TODO: should create a function to autopay all recurring expenses. Maybe later on, hope nikuwe na psyche.
@api_view(['GET'])
def get_bills(request):
    #get a list of all paid bills.
    bills = serialize('json', Bill.objects.filter(paid=True))

    return HttpResponse(bills, content_type='application/json')

@api_view(['GET'])
def pay_bill(request):
    pay_bill_request = json.loads(request.body) # serialize the json request to a python object
    bill = Bill(
        description=pay_bill_request['description'],
        amount = pay_bill_request['amount'],
        paid = True
    )
    bill.bill_type = Expense.objects.get(id=pay_bill_request['expense_id'])
    if  not pay_bill_request['remarks'].is_space():
        bill.remarks = pay_bill_request['remarks']
    bill.save()

    success_message = {
        "success": "successfully paid that bill"
    }

    return JsonResponse(success_message, safe=False)


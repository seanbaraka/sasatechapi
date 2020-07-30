from . import views
from django.urls import path
urlpatterns = [
    path('',views.expenses, name='expenses' ),
    path('bills', views.get_bills, name='bills'),
    path('paybill/', views.pay_bill, name='paybill')
]
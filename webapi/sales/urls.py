from . import views
from django.urls import path

urlpatterns = [
    path('', views.sales, name='sales'),
    path('record/', views.record_transaction, name='record'),
    path('product_sales/', views.product_sales, name='product_sales')
]
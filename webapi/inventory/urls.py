from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('inventory/', views.products, name='products'),
    path('inventory/add/', views.add_product, name='addproduct'),
    path('categories/', views.get_categories, name='categories'),
    path('categories/add/', views.add_category, name='addcategory')
]
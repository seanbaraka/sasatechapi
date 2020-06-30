from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('staff/', views.EmployeeView.as_view()),
    path('staff/register/', views.EmployeeView.as_view(), name='register'),
    path('staff/login/', views.userLogin, name='login')
]

# urlpatterns = [
#     url(r'^employees', EmployeeView.as_view())
# ]
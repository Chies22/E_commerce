from django.urls import path
from Customer import views

app_name = 'Customer'
urlpatterns = [
    path('customers/', views.customer_list, name='customer_list')
]
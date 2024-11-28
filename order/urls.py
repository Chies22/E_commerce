from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('orders/', views.order_list, name='order_list')
]
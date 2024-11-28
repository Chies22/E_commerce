from django.shortcuts import render,redirect
from .models import Customer, Order


# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def create_order(request):
    if request.method == 'POST':
        customer_id = request.POST['customer']
        total_amount = request.POST['total_amount']
        customer = Customer.objects.get(id=customer_id)
        order = Order.objects.create(customer=customer, total_amount=total_amount)
        return redirect('order_list')
    else:
        customers = Customer.objects.all()
        return render(request, 'create_order.html', {'customers': customers})

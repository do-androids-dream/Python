from django.shortcuts import render

# Create your views here.
def order(request):
    context = {'id': 'TEST'}
    return render(request, 'order/order.html', context)

def orders(request, id):
    context = {'id': id}
    return render(request, 'order/order.html', context)

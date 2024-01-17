from django.shortcuts import render
from store.models.order import Order
from django.views import View
# from store.middleware.auth import simple_middleware
# from django.utils.decorators import method_decorator

class Order_View(View):
    
    # @method_decorator(simple_middleware)

    def get(self,request):
        customer = request.session.get('customer')
        order = Order.get_orders_by_customer(customer)
        print(order)
        return render(request,'order.html',{'orders':order})
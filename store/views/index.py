from django.shortcuts import render,redirect , HttpResponse
from store.models.products import Product
from store.models.category import Category
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# store 
@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <=1 :
                        cart.pop(product)
                    else:
                        cart[product] = quantity -1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart',request.session['cart'])

            # print(product)
        return redirect('store')
        # return HttpResponse('cart',request.session['cart'])

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart={}
        product = None
        category = Category.get_all_category()
        # print(request.GET)
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_products_by_category_id(categoryID)
        else:
          product= Product.get_all_products()

        data = {'products':product,'category':category}
        print('you are',request.session.get('email'))
        # print(product)
        return render(request,'index.html',data)
     
   
     
          
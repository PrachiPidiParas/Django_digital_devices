from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$600000$peO7jXstsKk8r6yQJ91i8o$SygLWNVC+aa3fCWchc7nUVa5NP/Q4bjwVDKZRDgckhY='))


# Create your views here.
#homepage
def front(request):
    return render(request,'front.html')

# store 
def index(request):
    product = None
    category = Category.get_all_category()
    print(request.GET)
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.get_all_products_by_category_id(categoryID)
    else:
          product= Product.get_all_products()

    data = {'products':product,'category':category}
    print(product)
    return render(request,'index.html',data) 

# signup
def SignUp(request):
    if request.method == "GET":
        return render(request,'signup.html')
    else:
        postRequest = request.POST
        first_name = postRequest.get('Firstname')
        last_name = postRequest.get('Lastname')
        phone = postRequest.get('phone')
        email = postRequest.get('email')
        password = postRequest.get('password')
        print(first_name,last_name,phone,email,password)

        # validation
        values = {'firstname':first_name,'lastname':last_name,'phone':phone,'email':email}
        error_message = None
        customer = Customer(Firstname = first_name,
                            Lastname= last_name,
                            phone=phone,
                            email = email,
                            password=password)
        
        if not first_name:
            error_message ="Firstname Required !!"
        elif len(first_name) < 4:
            error_message = "firstname must be 4 char long or more"
        elif not last_name:
            error_message ="Lastname Required !!"
        elif len(first_name) < 4:
            error_message = "Lastname must be 4 char long or more"
        elif not phone:
            error_message ="Phone number Required  !!"
        elif len(phone) < 10:
            error_message = "Phone number must be 4 integer long or more"
        elif not password:
            error_message ="Password Required !!"
        elif len(password) < 4:
            error_message = "Password must be 6 char long or more"
        elif customer.isExists():
            error_message = "Email Already Exists !!"

    
        # saving
        
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('store')
        else:
            data = {'value':values,'error':error_message}
            return render(request,'signup.html',data)
    

    
# def Login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_byEmail(email)

#         error_message = None
#         if customer:
#             flag = check_password(password,customer.password)
#             if flag:
#                 return redirect('store')
#             else:
#                 error_message = "Email or Password Invalid !!"
#         else:
#             error_message = "Email or Password Invalid !!"

#         print(customer)
#         print(email,password)

#         return render(request,'login.html',{'error':error_message})

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_byEmail(email)

        error_message = None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                return redirect('store')
            else:
                error_message = "Email or Password Invalid !!"
        else:
            error_message = "Email or Password Invalid !!"

        print(customer)
        print(email,password)

        return render(request,'login.html',{'error':error_message})



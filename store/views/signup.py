from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

# signup
class SignUp(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        postRequest = request.POST
        first_name = postRequest.get('Firstname')
        last_name = postRequest.get('Lastname')
        phone = postRequest.get('phone')
        email = postRequest.get('email')
        password = postRequest.get('password')
        print(first_name,last_name,phone,email,password)
       
        # error_message = None
        customer = Customer(Firstname = first_name,
                            Lastname= last_name,
                            phone=phone,
                            email = email,
                            password=password)
        # ValidateCustomer(self.customer)
        error_message = self.ValidateCustomer(customer)
        
         # validation
        values ={'firstname':first_name,'lastname':last_name,'phone':phone,'email':email}

        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('store')
        else:
            data = {'value':values,'error':error_message}
            return render(request,'signup.html',data)
    
    # validate customer details
    def ValidateCustomer(self,customer):
        error_message = None
        if not customer.Firstname:
            error_message ="Firstname Required !!"
        elif len(customer.Firstname) < 4:
            error_message = "firstname must be 4 char long or more"
        elif not customer.Lastname:
            error_message ="Lastname Required !!"
        elif len(customer.Lastname) < 4:
            error_message = "Lastname must be 4 char long or more"
        elif not customer.phone:
            error_message ="Phone number Required  !!"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 4 integer long or more"
        elif not customer.password:
            error_message ="Password Required !!"
        elif len(customer.password) < 4:
            error_message = "Password must be 6 char long or more"
        elif customer.isExists():
            error_message = "Email Already Exists !!"
            
        return error_message


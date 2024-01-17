from django.contrib import admin
from django.urls import path
from .views.homepage import Front_view
from .views.index import Index
from .views.signup import SignUp 
from .views.login import Login
from .views.logout import Logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.order import Order_View
from .middleware.auth import simple_middleware

urlpatterns = [
    path('',Front_view.as_view(),name='homepage'),
    path('index',Index.as_view(),name='store'),
    path('signup',SignUp.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('checkout',CheckOut.as_view(),name='checkout'),
    path('order',simple_middleware(Order_View.as_view()),name='order_view'),
    
]

from . import views
from django.urls import path

urlpatterns=[
    path('',views.index),
    path('userreg',views.userreg),
    path('regTask',views.regTask),
    path('userlogin',views.userlogin),
    path('loginTask',views.loginTask),
    path('adminprofile',views.adminprofile),
    path('productshow',views.productshow),
    path('productlogin',views.productlogin),
    path('buy',views.buy),
    path('userprofile',views.userprofile),
    path('ulogout',views.ulogout),
    path('cart',views.cart),
    path('cartdesk',views.cartdesk),
    path('buyTask',views.buyTask),
    path('addproduct',views.addproduct),
    path('adminhistory',views.adminhistory),
    path('addproductTask',views.addproductTask),
    path('buyTaskdone',views.buyTaskdone),
    path('history',views.history),
    path('delete',views.delete),
    path('useradmindata',views.useradmindata),
    
   
]
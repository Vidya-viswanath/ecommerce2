from django.urls import path
from . import views

app_name="common"


urlpatterns=[
    path('',views.common_home,name="home"),
    path('customerreg',views.common_customerreg,name="custreg"),
    path('sellerreg',views.common_sellerreg,name="sellerreg"),
    path('customerlogin',views.common_customerlogin,name="custlog"),
    path('sellerlogin',views.common_sellerlogin,name="sellerlog"),
    path('emailcheck',views.check_email,name="check_email")
   
]
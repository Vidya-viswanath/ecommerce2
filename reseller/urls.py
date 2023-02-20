from django.urls import path
from . import views

app_name="reseller"

urlpatterns=[
    path('home',views.reseller_home,name="home"),
    path('product_catalogue',views.reseller_product_catalogue,name="catalogue"),
    path('add_product',views.reseller_add_product,name="addproduct"),
    path('update_stock',views.reseller_update_stock,name="stock"),
    path('change_password',views.reseller_change_password,name="password"),
    path('recent_order',views.reseller_recent_order,name="order"),
    path('orderhistory',views.reseller_orderhistory,name="history"),
    path('profile',views.reseller_profile,name="profile"),
     path('edit',views.reseller_edit,name="edit")
]
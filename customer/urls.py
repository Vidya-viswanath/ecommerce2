from django.urls import path
from . import views

app_name="customer"

urlpatterns=[
    path('home',views.customer_home,name="custhome"),
    path('productdetails/<int:pid>',views.customer_productdetails,name="details"),
    path('mycart',views.customer_mycart,name="cart"),
    path('delete/<int:id>',views.customer_delete,name="delete"),
    path('myorder',views.customer_myorder,name="order"),
    path('changepassword',views.customer_changepassword,name="password"),
    path('profile',views.customer_profile,name="profile"),
    path('edit',views.customer_edit,name="edit"),
    path('logout',views.customer_logout,name="logout")


]
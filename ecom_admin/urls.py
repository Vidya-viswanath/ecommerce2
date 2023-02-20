from django.urls import path
from . import views

app_name="ecom_admin"

urlpatterns=[
    # path('home',views.ecom_admin_home, name="home"),
    path('approve',views.ecom_admin_approve, name="approve"),
    path('views',views.ecom_admin_views, name="views"),
    path('viewc',views.ecom_admin_viewc, name="viewc"),
    path('home1',views.ecom_admin_home1, name="home1")


]
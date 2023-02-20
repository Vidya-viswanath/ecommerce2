from django.shortcuts import render

# Create your views here.
# def ecom_admin_home(request):
#     return render(request,'ecom_admin/home.html')

def ecom_admin_approve(request):
    return render(request,'ecom_admin/approve.html')

def ecom_admin_views(request):
    return render(request,'ecom_admin/views.html')

def ecom_admin_viewc(request):
    return render(request,'ecom_admin/viewc.html')

def ecom_admin_home1(request):
    return render(request,'ecom_admin/home1.html')
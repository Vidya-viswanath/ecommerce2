from django.shortcuts import render,redirect

from common.models import Customer, Seller
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse,HttpResponse
from . decorator import auth_customer

# Create your views here.
@auth_customer
def common_home(request):
    return render(request,'common/home.html')

def common_customerreg(request):
    if request.method == 'POST':
        customer_name = request.POST['c_name']
        customer_email = request.POST['c_email']
        customer_address = request.POST['c_address']
        customer_phone = request.POST['c_phone']
        customer_gender = request.POST['c_gender']
        customer_password = request.POST['c_password']

        new_customer = Customer(name=customer_name,
        email=customer_email,
        address=customer_address,
        phone=customer_phone,
        gender=customer_gender,
        password=customer_password)
        new_customer.save()
    return render(request,'common/customerreg.html')  
    

def common_sellerreg(request):
    if request.method == 'POST':
        seller_name = request.POST['s_name']
        seller_email = request.POST['s_email']
        seller_address = request.POST['s_address']
        seller_phone = request.POST['s_phone']
        seller_photo = request.FILES['s_photo']
        seller_company = request.POST['s_company']
        seller_accname = request.POST['s_account']
        seller_ifsc = request.POST['s_ifsc']
        seller_branch = request.POST['s_branch']
        seller_accnumber = request.POST['s_accnumber']
        seller_username = random.randint(1111,9999)
        seller_pass = 'seller-'+ str(seller_username) + seller_name

        new_seller = Seller(name=seller_name,
        email=seller_email,
        address=seller_address,
        phone=seller_phone,
        photo=seller_photo,
        comp_name=seller_company,
        acc_name=seller_accname,
        ifsc=seller_ifsc,
        branch=seller_branch,
        acc_number=seller_accnumber,
        username=seller_username,
        password=seller_pass)
        new_seller.save()
        message = 'HI YOUR USERNAME IS' + str(seller_username) + 'AND YOUR PASSWORD IS' + seller_pass


        send_mail('username and password',
        message,
        settings.EMAIL_HOST_USER,
        [seller_email,]

        
        )
    return render(request,'common/sellerreg.html')  

def common_customerlogin(request):
    msg = ""
    if request.method == 'POST':
        email = request.POST['c_username']
        password = request.POST['c_password']

        try :
            customer = Customer.objects.get(email = email, password = password)
            request.session['customer'] = customer.id
            return redirect('customer:custhome')

        except Exception as e :
            print(e)
            msg = 'Invalid username or Password'
            return render(request,'common/customerlogin.html',{'error':msg}) 

    return render(request,'common/customerlogin.html')

def common_sellerlogin(request):
    msg=""
    if request.method == 'POST' :
        s_user = request.POST['s_username']
        s_pass = request.POST['s_password']
        try : 
            seller = Seller.objects.get(username=s_user,password=s_pass)
            request.session['seller'] = seller.id 
            return redirect('reseller:home')
        except Exception as e :
            print(e)
            msg = 'Invalid username or password'
            
            return render(request,'common/sellerlogin.html',{'error':msg}) 
    return render(request,'common/sellerlogin.html')  

def check_email(request):
        print('jkkjhk')
        email = request.POST['email']   

        exist = Customer.objects.filter(email = email).exists()
        # return HttpResponse('hello')
        
        return JsonResponse({'status' : exist,})


        


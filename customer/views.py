from django.shortcuts import render,redirect
from common.models import Customer
from reseller.models import Product 
from . models import Cart
from . decorator import auth_customer

# Create your views here.
@auth_customer
def customer_home(request):
    # if 'customer' in request.session:
        products = Product.objects.all() #select * from product\
    #products = [
        #{
        # seller : 2,
        #product_name : 'smart watch', 
        #description : 'amazon bip3'
        #----
        # },
        #{
        #  # seller : 2,
        #product_name : 'smart watch', 
        #description : 'amazon bip3'
        # }
    # 
    # ]
    #we pass data from view to html in dictionary format
        return render(request,'customer/home.html',{'product_list': products})
    # else:
    #     return redirect('common:custlog')

@auth_customer
def customer_productdetails(request,pid):
    msg = ''
    product_data = Product.objects.get(id = pid) #fetching single data from table
    if request.method == 'POST' :
        product_id = request.POST['pid']

        item_exist = Cart.objects.filter(product_id = product_id, customer_id = request.session['customer']).exists()

        if not item_exist : # if item_exist == false


           cart_item = Cart(product_id = product_id, customer_id = request.session['customer'])
           cart_item.save()
           return redirect('customer:cart')

        else :
            msg = 'Item Already in Cart'   
    return render(request,'customer/productdetails.html',{'product':product_data,'msg':msg})

@auth_customer
def customer_mycart(request):
    cart = Cart.objects.filter(customer = request.session['customer'])
    # cart_data = Cart.objects.get(id = cid)
    # if request.method == 'POST' :
    #   cart_id = request.POST['cid']
      

    return render(request,'customer/mycart.html',{'cart': cart})

def customer_myorder(request):
    return render(request,'customer/myorder.html')

@auth_customer
def customer_changepassword(request):
    msg = ''
    if request.method == 'POST' :
        customer = Customer.objects.get(id = request.session['customer'])
        oldpass = request.POST['oldpass']
        newpass = request.POST['newpass']
        confirm = request.POST['confirm']
        if customer.password == oldpass:
            if newpass == confirm:
                customer.password = newpass
                customer.save()
                msg = 'password successfully changed'

            else :
                msg = 'password not matching'   

        else :
         msg = 'wrong password'            

    return render(request,'customer/changepassword.html',{'msg':msg})

def customer_profile(request):
    return render(request,'customer/profile.html')

@auth_customer
def customer_delete(request,id) :
    cart_item = Cart.objects.get(product = id, customer = request.session['customer']) 
    cart_item.delete()
    return redirect('customer:cart')

def customer_edit(request):
    return render(request,'customer/edit.html') 

def customer_logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:custlog')

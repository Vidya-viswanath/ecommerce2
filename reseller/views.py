from django.shortcuts import render

from reseller.models import Product

from common.models import Seller

# Create your views here.

def reseller_home(request):
    profile = Seller.objects.get(id = request.session['seller'])
    return render(request,'reseller/home.html',{'seller_prof' : profile})

def reseller_product_catalogue(request):
    products = Product.objects.filter(seller_id = request.session['seller'])
    return render(request,'reseller/product_catalogue.html',{'products' : products})

def reseller_add_product(request):
    if request.method == 'POST':
        product_name = request.POST['p_name']
        product_number = request.POST['p_number']
        product_description = request.POST['p_description']
        product_photo = request.FILES['p_photo']
        product_price = request.POST['p_price']
        product_stock = request.POST['p_stock']


        new_product = Product(name = product_name,
        number = product_number,
        description = product_description,
        image = product_photo,
        price = product_price,
        stock = product_stock,
        seller_id = request.session['seller']) 
        new_product.save()


    return render(request,'reseller/add_product.html')

def reseller_update_stock(request):
    return render(request,'reseller/update_stock.html')

def reseller_change_password(request):

    msg = ''
    if request.method == 'POST' :
        
        oldpass = request.POST['old_pass']
        newpass = request.POST['new_pass']
        confirm = request.POST['confirm']
        seller = Seller.objects.get(id = request.session['seller'])
        if seller.password == oldpass:
            if newpass == confirm:
                seller = Seller.objects.filter(id = request.session['seller']).update(password = newpass)
                # seller.password = newpass
                # seller.save()
                msg = 'password successfully changed'

            else :
                msg = 'password not matching'   

        else :
            msg = 'wrong password'     
    return render(request,'reseller/change_password.html',{'msg':msg})

def reseller_recent_order(request):
    return render(request,'reseller/recent_order.html')

def reseller_orderhistory(request):
    return render(request,'reseller/orderhistory.html')

def reseller_profile(request):
    profile = Seller.objects.get(id = request.session['seller'])

    return render(request,'reseller/profile.html',{'seller_prof' : profile})

def reseller_edit(request):
    return render(request,'reseller/edit.html')

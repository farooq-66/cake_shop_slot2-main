from django.shortcuts import render, redirect
from customerapp.models import Customer_tbl
from .models import cake_tbl

# Create your views here.
def view_dashboard(request):
    return render(request,'admin/dashboard.html')

def adminCustomers(request):
    customers = Customer_tbl.objects.all()     # SELECT * FROM users;
    return render(request,'admin/customers.html',{'users':customers})
 
def adminProducts(request):
    return render(request,'admin/products.html')

def adminAddProducts(request):
    if request.method == 'POST':
        cn = request.POST['cake_name']
        cp = request.POST['cake_price']
        cd = request.POST['cake_description']
        cc = request.POST['cake_category']
        ci = request.FILES['cake_image']

        obj = cake_tbl.objects.create(
            cake_name = cn,
            cake_price = cp,
            cake_description = cd, 
            cake_category = cc,
            cake_image = ci
        )
        if obj:
            return render(request,'admin/add-Product.html',{"sucess":"Cake uploaded sucessfully"})
        else:
            return render(request,'admin/add-Product.html',{"error":"cake not uploaded"})
    return render(request,'admin/add-Product.html')

def adminEditCustomer(request, customer_id):
    customer = Customer_tbl.objects.get(id=customer_id)
    if request.method == 'POST':
        # Take inputs from HTML form to single elements
        name = request.POST.get('customer_name')
        email = request.POST.get('customer_email')
        phone = request.POST.get('customer_phone')
        
        customer.customer_name = name
        customer.customer_email = email
        customer.customer_phone = phone
        
        customer.save()
        
        return redirect('adminCustomers')
    return render(request, 'admin/editCustomer.html', {'customer': customer})

def adminDeleteCustomer(request, customer_id):
    customer = Customer_tbl.objects.get(id=customer_id)
    customer.delete()
    return redirect('adminCustomers')


from .serializer import CakeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def cake_list(request):
    cakes = cake_tbl.objects.all()

    serializer = CakeSerializer(
        cakes,
        many = True
    )

    return Response(serializer.data)

@api_view(['POST'])
def add_cake(request):
    serializer = CakeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)
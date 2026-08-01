from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer_tbl

# Create your views here.
def home(request):
    return HttpResponse("Hello world")

def about(hello):
    return HttpResponse("About page")

def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        ue = request.POST.get('email')
        upass = request.POST.get('password')

        # print(ue,upass)
        obj = Customer_tbl.objects.filter(
            email = ue,
            password = upass
        )
        if obj:
            # print(obj.__dict__)
            for i in obj:
                request.session['user_id'] = i.id
            return render(request,'index.html')
        return render(request, 'login.html')
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        un = request.POST['user_name']
        ue = request.POST['email']
        up = request.POST['phone']
        upass = request.POST['password']

        obj = Customer_tbl.objects.create(
            username = un,
            email = ue,
            phone_no = up,
            password = upass
        )

        if obj:
            return render(request,'login.html')
        return render(request,'register.html')
    return render(request,'register.html')

from adminapp.models import cake_tbl

def view_products(request):
    cakes = cake_tbl.objects.all()
    # print(cakes.__dict__)
    return render(request,'products.html',{'cakes':cakes})



from .models import cart_tbl

def add_to_cart(request, cake_id):
    if 'user_id' not in request.session:
        return redirect('home-page')
    cake = cake_tbl.objects.get(id = cake_id)
    customer = Customer_tbl.objects.get(id = request.session['user_id'])

    cart_item, created = cart_tbl.objects.get_or_create(
        customer = customer,
        cake = cake
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view-products')

def view_cart(request):
    customer = Customer_tbl.objects.get(id = request.session['user_id'])

    cart_obj = cart_tbl.objects.filter(customer = customer)
    # print(cart_obj.__dict__)

    grand_total = sum(item.total_amount() for item in cart_obj)
    return render(request,'cart.html',{
            'cart_obj':cart_obj, 
            "grand_total":grand_total
        }
    )

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def cakeshop_info(request):
    return Response({
        "project":"Cakeshop",
        "backend":"Django",
        "frontend":"React",
        "database":"SQLite",
        "version":"1.0"
    })

from .serializer import CustomerSerializer


@api_view(['POST'])
def register(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':"Customer Registration Sucessfull",
            'data':serializer.data
        })
    return Response(serializer.errors)

import jwt
import datetime
from django.conf import settings


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    customer = Customer_tbl.objects.filter(
        email=email,
        password=password
    ).first()

    if not customer:
        return Response({
            "status":False,
            "message":"Invalid username or password!"
        }, status = 401)

    payload = {
        "customer_id":customer.id,
        "username" : customer.username,
        "email": customer.email,

        "exp" : datetime.datetime.utcnow() + 
                    datetime.timedelta(hours=1),
        "iat":datetime.datetime.utcnow()
    }

    access_token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm ="HS256"
    )
    return Response({
        "status":True,
        "message":"Login sucessful",
        "access_token":access_token
    })
from adminapp.serializer import CakeSerializer

from rest_framework.response import Response

@api_view(['GET'])
def get_all_cakes(request):
    cakes = cake_tbl.objects.all()
    serializer = CakeSerializer(cakes, many=True)
    return Response(serializer.data)
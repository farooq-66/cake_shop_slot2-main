from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns =[
    path('home/', views.home),
    path('about/',views.about, name="about-page"),
    path('home-page/', views.home_page,name='home-page'),
    path('login-page/',views.login_page, name='login_page'),
    path('register-page/',views.register_page, name='register-page'),
    path('view-products/',views.view_products, name='view-products'),
    path('cart/',views.view_cart, name="view-cart"),
    path('add-to-cart/<int:cake_id>',views.add_to_cart,name='add-to-cart'),

    path('api/cakeshop-info',views.cakeshop_info),
    path('api/register',views.register),
    path('api/login',views.login),
    path('api/getcakes/',views.get_all_cakes),

    path("token/",TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())

]
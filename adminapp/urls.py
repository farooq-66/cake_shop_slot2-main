from django.urls import path
from . import views

urlpatterns =[
    path('admin-dashboard/',views.view_dashboard, name='admin-dashboard'),
    path('customers/',views.adminCustomers, name= 'adminCustomers'),
    path('customers/edit/<int:customer_id>/', views.adminEditCustomer, name='adminEditCustomer'),
    path('customers/delete/<int:customer_id>/', views.adminDeleteCustomer, name='adminDeleteCustomer'),
    path('products/',views.adminProducts, name='adminProducts'),
    path('add-product',views.adminAddProducts, name='adminAddProducts'),

    path('api/cakes',views.cake_list)
]
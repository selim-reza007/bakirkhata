from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('all-customers/', views.customersListView, name='all-customers'),
    path('add-customer/', views.customerAddView, name='add-customer'),
    path('edit-customer/<int:cId>/', views.customerEditVIew, name='edit-customer'),
]

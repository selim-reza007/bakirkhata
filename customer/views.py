from django.shortcuts import render
from .forms import CreateCustomer

# Create your views here.
def customersListView(request):
    return render(request, 'customer/dashboard/list.html')

def customerAddView(request):
    form = CreateCustomer()
    return render(request, 'customer/dashboard/add.html', { 'form' : form })
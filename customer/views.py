from django.shortcuts import render, redirect
from django.db import DatabaseError
from django.core.exceptions import ValidationError
from .forms import CreateCustomer
from .models import Customer

# List view
def customersListView(request):
    data = Customer.objects.all()
    return render(request, 'customer/dashboard/list.html', { 'customers' : data })

# Add view with form submission and exception handling
def customerAddView(request):
    if request.method == 'POST':
        form = CreateCustomer(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('customer:all-customers')
        except ValidationError as e:
            form.add_error(None, f"Validation error: {e}")
        except DatabaseError as e:
            form.add_error(None, "A database error occurred. Please try again later.")
    else:
        form = CreateCustomer()

    return render(request, 'customer/dashboard/add.html', {'form': form})

def customerEditVIew(request, cId):
    customerObj = Customer.objects.get(id=cId)
    form = CreateCustomer(instance=customerObj)
    
    return render(request, 'customer/dashboard/add.html', {'form': form})
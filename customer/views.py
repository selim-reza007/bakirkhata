from django.shortcuts import render, redirect
from django.db import DatabaseError
from django.core.exceptions import ValidationError
from .forms import CreateCustomer

# List view
def customersListView(request):
    return render(request, 'customer/dashboard/list.html')

# Add view with form submission and exception handling
def customerAddView(request):
    if request.method == 'POST':
        form = CreateCustomer(request.POST)
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
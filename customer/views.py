from django.shortcuts import render

# Create your views here.
def customersListView(request):
    return render(request, 'customer/dashboard/list.html')
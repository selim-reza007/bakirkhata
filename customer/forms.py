from django import forms
from .models import Customer

class CreateCustomer(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ("name", "address", "mobile", "balance", "picture")


#front end goes data to backend

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id','name','price','description']  
        #migration karne ke bad id create hoti hai
        
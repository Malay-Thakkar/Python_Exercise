from django import forms
from .models import product

class stockForm(forms.Form):
    product_name=forms.CharField(max_length=120)
    product_id=forms.CharField(max_length=120)
    product_price=forms.CharField(max_length=120)
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

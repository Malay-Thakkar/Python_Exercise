from django import forms


class stockForm(forms.Form):
    product_name=forms.CharField(max_length=120)
    product_id=forms.CharField(max_length=120)
    product_price=forms.CharField(max_length=120)
    
class productForm(forms.Form):
    product_name=forms.CharField(max_length=120)
    product_id=forms.CharField(max_length=120)
    product_dict=forms.CharField(max_length=120)
    product_price=forms.CharField(max_length=120)
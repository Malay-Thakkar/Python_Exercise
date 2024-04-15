from .models import ProfileModel
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

# forms.py regular form give more control on validation and model,crisp form gives all model filed and use model validation  
from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    address = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Custom validation for phone number
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone

    
class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name', 'address', 'phone', 'email']
        
        

from django import forms
from .models import signup,filesModel
    
class signupForm(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'
        
class FileForm(forms.ModelForm):
    class Meta:
        model = filesModel
        fields = ('files',)
        widgets = {
            "files": forms.ClearableFileInput(attrs={'id': 'files', 'required': True})
        }
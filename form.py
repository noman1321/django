# listings/forms.py
from django import forms
from .model import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'address', 'city', 'country', 'phone', 'website', 'email']

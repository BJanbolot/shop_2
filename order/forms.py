from .models import Order
from django import forms

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('postal_code', 'city')
        
    
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    closing_time = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Ensure this matches the format users will input
        widget=forms.DateInput(attrs={
            'class': 'form-control date-picker',
            'placeholder': 'YYYY-MM-DD',
            'type': 'date'  # This will use the browser's date picker
        })
    )
    class Meta:
        model = Product
        fields = ['productname','content','image', 'closing_time', 'starting_price']

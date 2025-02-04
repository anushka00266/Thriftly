from django import forms
from .models import Item, Order

# Input styling class
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border-2 border-gray-300 focus:ring-teal-500 focus:outline-none'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image')  # Fields for new item
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')  # Fields for editing item
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'is_sold': forms.CheckboxInput(attrs={'class': INPUT_CLASSES}),
        }

class ShippingDetailsForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES}),
        label="Full Name"
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': INPUT_CLASSES}),
        max_length=1024,
        label="Shipping Address"
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES}),
        label="Phone Number"
    )
    city = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES}),
        label="City"
    )
    postal_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES}),
        label="Postal Code"
    )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_full_name', 'shipping_address', 'shipping_phone_number', 'shipping_city', 'shipping_postal_code']
        widgets = {
            'shipping_full_name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'shipping_address': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'shipping_phone_number': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'shipping_city': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'shipping_postal_code': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }

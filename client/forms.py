from django.forms import ModelForm
from .models import user_info
from django import forms



class information_form(ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    phone_number = forms.CharField(min_length=10,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    image = forms.ImageField(label='Upload Image', required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model= user_info
        fields="__all__"
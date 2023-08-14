from django import forms
from django.forms import ModelForm
from .models import *

class AptForm(ModelForm):
    class Meta:
        model = Appartement
        fields = ["city", "status", "occupied", "address", "is_fork", "price",
                 "period", "size", "tage", "rooms", "bathroom",
                 "kitchen", "image1", "image2", "image3", "image4", "image5", "description"]
        widgets = {
            'city': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'occupied': forms.CheckboxInput(),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'period': forms.Select(attrs={'class':'form-control'}),
            'size': forms.NumberInput(attrs={'class':'form-control'}),
            'tage': forms.Select(attrs={'class':'form-control'}),
            'rooms': forms.NumberInput(attrs={'class':'form-control'}),
            'bathroom': forms.NumberInput(attrs={'class':'form-control'}),
            'kitchen': forms.NumberInput(attrs={'class':'form-control'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
            'image4': forms.FileInput(attrs={'class':'form-control'}),
            'image5': forms.FileInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'})
        }
        
class EditPost(ModelForm):
    class Meta:
        model = Appartement
        fields = ["status", "occupied", "address", "price", "period", "image1", "image2", "image3", "image4", "image5",]
        widgets = {
            'status': forms.Select(attrs={'class':'form-control'}), 
            'occupied': forms.CheckboxInput(),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'period': forms.Select(attrs={'class':'form-control'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
            'image4': forms.FileInput(attrs={'class':'form-control'}),
            'image5': forms.FileInput(attrs={'class':'form-control'}),
        }


class EditProfile(ModelForm):
    class Meta:
        model = Renter
        fields = ["phone", 'address', "image"]
        widgets = {
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
            'address': forms.TextInput(attrs={"class": "form-control"}),
            'image': forms.FileInput(attrs={"class": "form-control"}),
            
        }
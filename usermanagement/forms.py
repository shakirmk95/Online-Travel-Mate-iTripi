from django import forms

from usermanagement.models import UserImage


class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        label='Upload Your Image',
        # help_text='max. 42 megabytes'
    )

class TransportForm(forms.Form):
	make = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-5','placeholder': 'Make'}))
	car = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Car'}))
	varient = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Varient'}))
	color = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Color '}))
	seats = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Seats'}))
	image = forms.ImageField(label = "Upload Your Car Image")

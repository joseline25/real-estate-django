from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        #fields = '__all__'
        exclude = ["status", "owner"]
        
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['listing', 'price']
        
        widgets = {
            'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                                            'date',
                                                                    'type': 'date'}) ,
            'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                                            'date',
                                                                    'type': 'date'}),
        }
        
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1',  'password2']
        
 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
        

        

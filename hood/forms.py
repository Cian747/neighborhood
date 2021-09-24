from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Meeting,Business

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1','password2' ]

        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.TextInput(attrs = {'class':'form-control ','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.TextInput(attrs = {'class':'form-control', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['family_name','profile_photo','hood','family_email','family_members']

        widgets = {
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'profile_photo':forms.FileInput(attrs={'class':'form-control'}),
            'family_email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter your email address'}),
        }

class RegisterBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','neighbor','description','business_email','image']

        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Business name...'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Business description...'}),
            'neighbor':forms.Select(attrs={'class': 'form-control'}),
            'business_email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Business email..'}),
        }

class EditBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','neighbor','description']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Business name...'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Business description...'}),
            'neighbor':forms.Select(attrs={'class': 'form-control'}),
        }

class PostMessageForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title','content']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Topic...'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Write a message...'}),
        }


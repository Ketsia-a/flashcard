from django import forms
from .models import Card, Profile, Subject
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name', 'bio']

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title','note','image']

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')





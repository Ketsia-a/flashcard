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
        fields = ['title','note','image','subject']

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')





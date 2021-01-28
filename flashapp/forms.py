from django import forms
from .models import Card, Profile, Subject
from django.contrib.auth.models import User

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name', 'bio']

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title','note','image']

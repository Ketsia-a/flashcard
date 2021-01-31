from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CardForm,UpdateUserProfileForm
from .models import  Profile,Card,Subject
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import SignUpForm, CardForm,UpdateUserProfileForm
from django.contrib.auth import authenticate,login
# Create your views here.


def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register/registration_form.html', {'form': form})

def profile(request, username):
    cards = request.user.profile.cards.all()
    subjects = Subject.get_subjects()
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    if request.method == "POST":
        form = CardForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user.profile
            card.save()
    else:
        form = CardForm()

    context = {
        'prof_form': prof_form,
        'cards': cards,
        'form':form,
        'subjects':subjects,

    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def card_category(request, subject):
    current_user = request.user
    cards = Card.filter_by_subject(subject)
    subjects = Subject.get_subjects()
    context = {
    'cards':cards,
    'subjects': subjects
    }
    return render(request,'subject.html',context)    


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('home')
#     else:
#           return ('invalid login..')
      
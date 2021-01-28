from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CardForm,UpdateUserProfileForm
from .models import  Profile,Card,Subject
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request,'home.html')

def profile(request, username):
    cards = request.user.profile.cards.all()
    subject = Subject.objects.all()
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
        'subject':subject,

    }
    return render(request, 'profile.html', context)

def card_category(request, location):
    cards = Card.filter_by_subject(subject)
    current_user = request.user
    subjects = Subject.get_subjects()
    context = {'cards':cards,'subjects': subjects}
    return render(request,'subject.html',context)    
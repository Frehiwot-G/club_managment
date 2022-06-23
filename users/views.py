from __future__ import division
from django.contrib.auth import authenticate,login,logout
from pyexpat.errors import messages
from django.shortcuts import redirect, render

from users.models import Division
from .forms import NewMemberForm,DivisionForm
from django.contrib.auth.decorators import login_required

def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    div=Division.objects.all()
    form =NewMemberForm()
    # f =DivForm()
    if request.method == 'POST':
        form =NewMemberForm(request.POST)
        # f =DivForm(request.POST) 
        if form.is_valid():
            # # username = form.cleaned_data('post')
            # form =NewMemberForm()
            form.save()
            # f.save()
    context={'form':form , 'div':div}
    return render(request, 'register.html', context)
@login_required(login_url='login')
def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
            # messages(request, 'username or password is incorrect')
            
    context={}
    return render(request, 'login.html', context)

def homePage(request):
    context={}
    return render(request, 'home.html', context)


def divPage(request):
    form =DivisionForm()
    if request.method == 'POST':
        form =DivisionForm(request.POST) 
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'div.html', context)
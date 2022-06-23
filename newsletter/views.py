from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import MailForm,MailallForm
from django.core.mail import send_mail
from django.conf import settings
from django_pandas.io import read_frame
from users.models import *

def division_mailPage(request):
    form =MailForm() 
    # emails=Member.objects.all()
    # df=read_frame(emails, fieldnames=['email'])
    # mail_list=df['email'].values.tolist()
    if request.method == 'POST':
        form =MailForm(request.POST) 
        if form.is_valid():
            form.save()
            div=request.POST['division']
            print(div)
            emails=Member.objects.filter(division_id=div)
            df=read_frame(emails, fieldnames=['email'])
            mail_list=df['email'].values.tolist()
            tittle=form.cleaned_data.get('title')
            message=form.cleaned_data.get('message')
            send_mail(
                tittle,
                message,
                settings.EMAIL_HOST_USER,
                mail_list,
                fail_silently=False,)
            messages.success(request, 'Message has been sent.')
            return redirect('mail')
    context={'form':form}
    return render(request, 'mail.html', context)

def mailPage(request):
    form =MailallForm()
    emails=Member.objects.all()
    df=read_frame(emails, fieldnames=['email'])
    mail_list=df['email'].values.tolist()
    if request.method == 'POST':
        form =MailallForm(request.POST) 
        if form.is_valid():
            form.save()
            tittle=form.cleaned_data.get('title')
            message=form.cleaned_data.get('message')
            send_mail(
                tittle,
                message,
                settings.EMAIL_HOST_USER,
                mail_list,
                fail_silently=False,)
            messages.success(request, 'Message has been sent.')
            return redirect('mail')
    context={'form':form}
    return render(request, 'all_mail.html', context)

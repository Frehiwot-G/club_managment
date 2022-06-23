from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CommentForm,AdminForm
from django.core.mail import send_mail
from django.conf import settings
from django_pandas.io import read_frame
from users.models import *
from .models import *


def commentPage(request):
    form =AdminForm()
    if request.method == 'POST':
        form =AdminForm(request.POST) 
        if form.is_valid():
            form.save()
            
    context={'form':form}
    return render(request, 'comment.html', context)
# def adminPage(request):
    # forms =AdminForm()
    # # comm=form.cleaned_data.get('comment')
    # # name=request.POST['username']
    # # print(name)
    # comments=Comment.objects.all()
    # # df=read_frame(comments, fieldnames=['comment'])
    # # comm_list=df['comment'].values.tolist()
    # if request.method == 'POST':
    #     forms =AdminForm(request.POST) 
    #     if forms.is_valid():
    #            forms.update()

    #         # username.save()
    #     # accept=forms.cleaned_data['accept']
    #     # print(accept)
    #         # comments=Member.objects.filter(username_id=name)
    #         # df=read_frame(comments, fieldnames=['comment'])
    #         # comm_list=df['comment'].values.tolist()
    # context={'forms':forms,'comments':comments}
    # return render(request, 'admin.html', context)
def adminPage(request,id):
    item=Comment.objects.get(pk=id)
    updateForm=CommentForm(instance=item)
    if request.method=='POST':
        todoAdd=CommentForm(request.POST,instance=item)
        if todoAdd.is_valid():
            todoAdd.save()
            # messages.success(request, 'Data has been updated.')
            return redirect('/comment/item/edit/'+str(id))
    return render(request,'update.html',{
        'form':updateForm,
        'item':item
    })
# from django.forms import ModelForm
import datetime
from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

YEARS= [x for x in range(2015,datetime.date.today().year+1)]

class NewMemberForm(UserCreationForm, forms.ModelForm):
    year= forms.DateField(widget=forms.SelectDateWidget(years=YEARS),initial="2015-09-20")
    # div=Member.division.all()
    # division=forms.CheckboxSelectMultiple(choices=div)
    class Meta(UserCreationForm):
        model = Member
        fields = ('username','email','first_name','last_name','division','female','year','male','password1','password2')
class DivisionForm(forms.ModelForm):
    class Meta():
        model = Division
        fields= '__all__'
# class DivForm(forms.ModelForm):
#     # div=Member.division.all()
#     # division=forms.MultipleChoiceField(div)
#     class Meta():
#         model = Division
#         fields=('name')



from dataclasses import fields
import imp
from django import forms
from .models import *



class MailForm(forms.ModelForm):
    class Meta:
        model=Message
        fields='__all__'
class MailallForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['title','message']


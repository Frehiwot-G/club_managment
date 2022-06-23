from django import forms
from .models import *



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'
class AdminForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['username','comment']
from itertools import product
from django.contrib import admin

from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import NewMemberForm

class CustomUserAdmin(UserAdmin):
    form = NewMemberForm
    model = Member
    list_display = ["email", "username","first_name","last_name","cpd","DEV","ICPC","password1","password2"]

admin.site.register(Member)
admin.site.register(Division)


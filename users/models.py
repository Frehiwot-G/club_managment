from random import choices
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


class Division(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class Member(AbstractUser):
    # div=Division.objects.name
    # div=(
    #     ('cpd','cpd'),
    #     ('DEV','DEV'),
    #     ('ICPC','ICPC'),
    # )
    division=models.ForeignKey(Division, on_delete=models.SET_NULL,  null=True)
    # division=models.ManyToManyField(Division)
    # cpd=models.BooleanField("cpd", default=False)
    # DEV=models.BooleanField("DEV", default=False)
    # ICPC=models.BooleanField("ICPC", default=False)
    female=models.BooleanField("female", default=False)
    male=models.BooleanField("male", default=False)
    year=models.DateField(null=True)
    def __str__(self):
        return self.username

from __future__ import division
from email import message
from turtle import title
from django.db import models
from users.models import *

class Message(models.Model):
    division=models.ForeignKey(Division, on_delete=models.SET_NULL,  null=True)
    title=models.CharField(max_length=200,null=True)
    message=models.TextField(max_length=1000,null=True)
    def __str__(self):
        return self.title

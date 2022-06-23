from django.db import models
from users.models import *

class Comment(models.Model):
    # username=models.ForeignKey(Member, on_delete=models.SET_NULL,  null=True)
    username=models.CharField(max_length=200,null=True)
    comment=models.TextField(max_length=1000,null=True)
    accept=models.BooleanField("accept", default=False)
    def __str__(self):
        return self.username

# class Accepted(models.Model):
#     username=models.CharField(max_length=1000,null=True)
#     # comment=models.TextField(max_length=1000,null=True)
#     accepted=models.BooleanField("accept", default=False)
#     def __str__(self):
#         return self.username
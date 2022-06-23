from django.urls import path
from . import views
urlpatterns=[
path('division',views.division_mailPage,name='mail'),
path('',views.mailPage,name='all_mail'),
]
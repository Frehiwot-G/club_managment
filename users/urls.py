from django.urls import path
from . import views
urlpatterns=[
path('register/',views.registerPage,name='register'),
path('login/',views.loginPage,name='login'),
path('home/',views.homePage,name='home'),
path('div/',views.divPage,name='div'),
]
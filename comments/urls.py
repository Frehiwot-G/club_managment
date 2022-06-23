from django.urls import path
from . import views
urlpatterns=[
path('',views.commentPage,name='comment'),
# path('ad/',views.adminPage,name='admin'),
path('item/edit/<int:id>',views.adminPage,name='admin'),
]
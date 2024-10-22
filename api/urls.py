from django.urls import path
from . import views

urlpatterns =  [
    path('blogposts/',views.BLogPostListCreate.as_view(), name = 'blogpost-view-create')
]
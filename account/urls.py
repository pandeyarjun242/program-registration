from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
path('',views.Home.as_view(), name = "home"),
path('signup/', views.Signup.as_view(), name = "signup"),
path('contact',views.Contact.as_view(), name = "contact")
]

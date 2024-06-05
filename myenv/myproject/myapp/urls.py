from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('menu',views.menu,name='menu'),
    path('blog',views.blog,name='blog'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('team',views.team,name='team'),
    path('rest',views.rest,name='rest'),
    path('register',views.signup,name='signup')
]
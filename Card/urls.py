from django.urls import path
from .views import *

urlpatterns = [
    path('signup',customerRegister,name='signup'),
    path('',customerLogin,name='login'),
    path('home',Home,name='home'),
    path('index',Index,name='index'),
    path('services',Services,name='services'),
    path('logout',Signout,name='logout'),
    path('contact',ContactView.as_view(),name='contact'),
    path('about', About,name='about'),
    path('addrationcard',AddPostView.as_view(),name='AddRationCard'),
    path('update/<int:pk>',UserUpdateView.as_view(), name='update'),
    path('cancel',CancelRationCard.as_view(), name='cancel'),
    path('dashboard',DeshboardView.as_view(),name='dashboard'),
]
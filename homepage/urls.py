from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
      path('', views.homepage),
      # path('sign_in/', views.sign_in),
      # path('register/', views.user_login),


]
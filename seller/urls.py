from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='seller-home'),
      path('about/', views.About, name='seller-about'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('sing_up/', views.sing_up, name='sing_up'),
    path('login/', views. Loginview.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
 
]
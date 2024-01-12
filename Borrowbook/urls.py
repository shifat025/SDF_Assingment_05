from django.urls import path
from . import views

urlpatterns = [
    path('borrow/<int:id>/', views.borrow, name='borrow'),
    path('bookreturn/<int:id>/<int:historyid>/', views.bookreturn, name='bookreturn')
]

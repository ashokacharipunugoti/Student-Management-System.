from django.urls import path
from StudentApp import views

urlpatterns = [
    path('', views.login, name='login' ),
    path('register', views.register, name='register' ),
    path('add/', views.add, name='add' ),
    path('home/', views.home, name='home'),
    path('list/', views.list_of_students, name='list'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.deletefun, name='delete'),
]

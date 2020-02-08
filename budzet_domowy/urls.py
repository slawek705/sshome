from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.start_page_view, name='app_budzet_domowy'),
    path('asd/', include('blog.urls'), name='blogapp'),
    #path('/login/', views.user_login, name='login')

]
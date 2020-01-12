from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.start_page_view, name='app_budzet_domowy'),
    path('djangogirls/', include('blog.urls'), name='blogapp'),
]
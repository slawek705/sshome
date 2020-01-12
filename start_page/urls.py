from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.start_page_view, name='start_page'),
    path('admin/', admin.site.urls, name='admin_sites'),
    path('djangogirls/', include('blog.urls'), name='blogapp'),
]
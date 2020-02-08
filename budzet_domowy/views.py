from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def start_page_view(request):
    return render(request, 'budzet_domowy/base.html', {'ads': ['lad', 'asd']})


def logout_view(request):
    return logout(request)

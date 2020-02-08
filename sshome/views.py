from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


def start_page_view(request):
    return render(request, 'sshome/main.html', {'ads': ['lad', 'asd']})

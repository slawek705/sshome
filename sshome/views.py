from django.shortcuts import render, get_object_or_404

def start_page_view(request):
    return render(request, 'sshome/base.html', {'ads': ['lad', 'asd']})

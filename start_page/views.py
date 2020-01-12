from django.shortcuts import render, get_object_or_404

def start_page_view(request):
    return render(request, 'start_page/base.html', {'ads': ['lad', 'asd']})

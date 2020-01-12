from django.shortcuts import render, get_object_or_404

def start_page_view(request):
    return render(request, 'budzet_domowy/base.html', {'ads': ['lad', 'asd']})

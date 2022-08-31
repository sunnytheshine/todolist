from django.shortcuts import render

def home(request):
    ''' Renders home page '''

    content = {
        'list': '',
    }
    return render(request, 'home.html', content)
from django.shortcuts import render

def home(request):
    context = {
        'name': 'Madina',
        'age': 15,
    }
    return render(request, 'home/index.html', context)
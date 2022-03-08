from django.shortcuts import render

# Create your views here.
def HomeView(request, *args, **kwargs):
    return render(request, 'index.html', {})

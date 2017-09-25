from django.shortcuts import render


# Create your views here.
def index(request):
    # The home view
    return render(request, 'index.html')

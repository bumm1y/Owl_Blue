from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'owl_blue_app/index.html')


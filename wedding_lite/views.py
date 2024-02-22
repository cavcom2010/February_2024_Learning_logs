from django.shortcuts import render
from .import views

# Create your views here.
def index_view(request):
    return render(request, 'index.html')


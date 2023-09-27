from django.shortcuts import render

# Create your views here.
def show_ermakov(request):
    return render(request,'ermakov/ermakov.html')
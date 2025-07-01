from django.shortcuts import render, redirect

# Create your views here.

def subjects_view(request):
    

    return render(request, 'subjects.html')
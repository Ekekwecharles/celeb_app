from django.shortcuts import render, redirect
from .models import Celebrity

def show_celebrities(request):
    celebrities = Celebrity.objects.all()
    context = {'celebrities': celebrities}
    return render(request, 'celeb_app/show_celebrities.html', context)

def vote_celebrity(request):
    # Logic to handle voting
    # Update the votes for the selected celebrity
    return redirect('show_celebrities')

def enter_token(request):
    return render(request, 'enter_token.html')

def thank_you(request):
    return render(request, 'thank_you.html')

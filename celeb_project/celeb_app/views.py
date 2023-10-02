from django.shortcuts import render, redirect
from .models import Celebrity
from django.contrib import messages

def show_celebrities(request):
    celebrities = Celebrity.objects.all()
    context = {'celebrities': celebrities}
    return render(request, 'celeb_app/show_celebrities.html', context)

def vote_celebrity(request):
    # Logic to handle voting
    # Update the votes for the selected celebrity
    return redirect('show_celebrities')


def enter_token(request):
    celebrity_id = request.GET.get('celebrity_id')
    token = request.GET.get('token')

    # Assuming celebrity_id is an integer and corresponds to a valid Celebrity
    celebrity = Celebrity.objects.get(id=celebrity_id)

    # celebrity_id = int(celebrity_id)

    if celebrity_id == '2':
        if token and token.startswith('E') and token.endswith('C') and token[1:-1].isdigit():
            # Token is valid, increase votes for the celebrity
            celebrity.votes += 1
            celebrity.save()
            # return render(request, 'thank_you.html')
            messages.success(request, "Thanks for your vote, You are Indeed a real fan❤❤❤ \nRefer to your friends for more votes")
        else:
            messages.error(request, 'Incorrect Token')

    else:
        messages.error(request, 'This Poll link is only for Emilia Clarke, find alternate links to vote for others')
    # Token is invalid, redirect to an error page or handle it accordingly
    # return render(request, 'invalid_token.html')

    return redirect('show_celebrities')


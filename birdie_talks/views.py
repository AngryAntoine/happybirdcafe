from django.shortcuts import render

# Create your views here.


def birdie_talks(request):
    return render(request, 'birdie_talks/lets_talk_about_the_birds.html')

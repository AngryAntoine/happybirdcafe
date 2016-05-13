from django.shortcuts import render

# Create your views here.


def greeting_page(request):
    return render(request, 'home/greeting_page.html')

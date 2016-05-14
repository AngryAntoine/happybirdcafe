from django.shortcuts import render
from .models import Greeting
# Create your views here.


def greeting_page(request):
    greeting = Greeting.objects.all()
    return render(request, 'home/greeting_page.html', {'greeting': greeting})

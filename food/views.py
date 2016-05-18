from django.shortcuts import render, get_object_or_404
from .models import Food

# Create your views here.


def food(request):
    foods = Food.objects.all()
    return render(request, 'food/food.html',
                  {'foods': foods})


def food_details(request, food_id):
    foods = get_object_or_404(Food, id=food_id)
    food_detail = get_object_or_404(Food, id=food_id)
    return render(request, 'food/food_detail.html',
                  {'foods': foods,
                   'food_detail': food_detail})

from django.shortcuts import render, redirect
from .models import Dish
import random
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
import requests


def get_food_image(request):
    api_url = f"https://api.unsplash.com/photos/random?query=food&client_id={settings.UNSPLASH_ACCESS_KEY}"
    response = requests.get(api_url)
    data = response.json()
    image_url = data["urls"]["regular"]
    return JsonResponse({"image_url": image_url})


def home(request):
    dishes = Dish.objects.all()
    dish = random.choice(dishes) if dishes else None
    return render(request, "meals/home.html", {"dish": dish})


@login_required
def add_dish(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Dish.objects.create(name=name)
            return redirect("home")
    return render(request, "meals/add_dish.html")


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, "meals/dish_list.html", {"dishes": dishes})


@login_required
def update_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            dish.name = name
            dish.save()
            return redirect("dish_list")
    return render(request, "meals/update_dish.html", {"dish": dish})


@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == "POST":
        dish.delete()
        return redirect("dish_list")
    return render(request, "meals/delete_dish.html", {"dish": dish})

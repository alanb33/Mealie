from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import FoodItem

# A separate view file for the experimental route, to isolate imports.

def view_food_db(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Mealie:login"))
    else:
        debug_msg = str(len(FoodItem.objects.all()))
        food_db_json = serializers.serialize("json", FoodItem.objects.all())

        return render(request, "MealieApp/experimental/view_food_db.html",
        {
            "title": "EXPERIMENTAL View Food DB",
            "script_src": "MealieApp/js/experimental/view_food_db.js",
            "food_db_json": food_db_json,
        })

def add_food_form(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Mealie:login"))
    else:
        if request.method == "POST":
            food_name = request.POST["food-name"]
            food_ss = request.POST["food-serving-size"]
            return HttpResponse(f"Nice, the food is {food_name} and the serving size is {food_ss}.")
        else:
            return render(request, "MealieApp/experimental/add_food_form.html",
            {
                "title": "EXPERIMENTAL Add Food Form",
            })
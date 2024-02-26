from django.core import serializers
from django.shortcuts import render
from .models import FoodItem

# A separate view file for the experimental route, to isolate imports.

def view_food_db(request):

    debug_msg = str(len(FoodItem.objects.all()))
    food_db_json = serializers.serialize("json", FoodItem.objects.all())

    return render(request, "Mealieapp/experimental/view_food_db.html",
    {
        "title": "EXPERIMENTAL View Food DB",
        "script_src": "MealieApp/js/experimental/view_food_db.js",
        "food_db_json": food_db_json,
    })
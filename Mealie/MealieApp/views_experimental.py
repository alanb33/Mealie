from django.core import serializers
from django.shortcuts import render
from .models import FoodItem

# A separate view file for the experimental route, to isolate imports.

def debugger(request):

    debug_msg = str(len(FoodItem.objects.all()))
    food_db_json = serializers.serialize("json", FoodItem.objects.all())
    
    return render(request, "Mealieapp/debugger.html",
    {
        "title": "Debugger Page",
        "script_src": "MealieApp/js/debugger.js",
        "food_db_json": food_db_json,
    })
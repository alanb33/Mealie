from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import FoodItem
from .auth_util import redirect

# A separate view file for the experimental route, to isolate imports.

def view_food_db(request):
    redirected = redirect(request, "superuser")
    if not redirected:
        food_db_json = serializers.serialize("json", FoodItem.objects.all().order_by("name"))

        return render(request, "MealieApp/experimental/view_food_db.html",
        {
            "title": "EXPERIMENTAL View Food DB",
            "script_src": "MealieApp/js/experimental/view_food_db.js",
            "food_db_json": food_db_json,
        })
    else:
        return redirected

def add_food_form(request):
    redirected = redirect(request, "superuser")
    if not redirected:
        all_food_names = serializers.serialize("json", FoodItem.objects.only("name"))
        if request.method == "POST":
            new_food = FoodItem(
                name = request.POST["food-name"],
                serving_size = request.POST["food-serving-size"],
                calories = request.POST["food-calories"],
                total_fat_dv = request.POST["food-total-fat-dv"],
                saturated_fat_dv = request.POST["food-saturated-fat-dv"],
                trans_fat_dv = request.POST["food-trans-fat-dv"],
                cholesterol_dv = request.POST["food-cholesterol-dv"],
                sodium_dv = request.POST["food-sodium-dv"],
                total_carbohydrates_dv = request.POST["food-total-carbohydrates-dv"],
                dietary_fiber_dv = request.POST["food-dietary-fiber-dv"],
                total_sugars = request.POST["food-total-sugars"],
                added_sugars_dv = request.POST["food-added-sugars-dv"],
                protein = request.POST["food-protein"],
                vitamin_d_dv = request.POST["food-vitamin-d-dv"],
                calcium_dv = request.POST["food-calcium-dv"],
                iron_dv = request.POST["food-iron-dv"],
                potassium_dv = request.POST["food-potassium-dv"],
            )
            new_food.save()
            return render(request, "MealieApp/experimental/add_food_form.html",
            {
                "title": "EXPERIMENTAL Add Food Form",
                "script_src": "MealieApp/js/experimental/add_food_form.js",
                "success_msg": f"{request.POST['food-name']} added to the database!",
                "all_food_names": all_food_names,
            })
        else:         
            return render(request, "MealieApp/experimental/add_food_form.html",
            {
                "title": "EXPERIMENTAL Add Food Form",
                "script_src": "MealieApp/js/experimental/add_food_form.js",
                "all_food_names": all_food_names,
            })
    else:
        return redirected
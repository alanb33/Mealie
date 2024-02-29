from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import FoodItem, JournalEntry
from .auth_util import redirect

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Mealie:login"))
    else:
        greet_msg = ""
        if request.user.first_name:
            greet_msg = request.user.first_name
        else:
            greet_msg = request.user.username
        return render(request, "MealieApp/index.html",
        {
            "title": "Mealie!",
            "user_name": greet_msg
        })

def login_view(request):
    print(request.path)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Returns User if valid or None/raise error otherwise
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("Mealie:index"))
        else:
            return render(request, "MealieApp/login.html",
            {
                "title": "Mealie!",
                "warn_msg": "Username or password incorrect."
            })
    else:
        if not request.user.is_authenticated:
            return render(request, "MealieApp/login.html",
            {
                "title": "Mealie!"
            });
        else:
            return HttpResponseRedirect(reverse("Mealie:index"))

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "MealieApp/login.html",
        {
            "title": "Mealie!",
            "warn_msg": "You have been logged out."
        })
    else:
        return render(request, "MealieApp/login.html",
        {
            "title": "Mealie!",
            "warn_msg": "You are not logged in."
        })

def view_food_db(request):
    redirected = redirect(request, "superuser")
    if not redirected:
        food_db_json = serializers.serialize("json", FoodItem.objects.all().order_by("name"))

        return render(request, "MealieApp/view_food_db.html",
        {
            "title": "View Food Database",
            "script_src": "MealieApp/js/view_food_db.js",
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
            return render(request, "MealieApp/add_food_form.html",
            {
                "title": "Add New Food",
                "script_src": "MealieApp/js/add_food_form.js",
                "success_msg": f"{request.POST['food-name']} added to the database!",
                "all_food_names": all_food_names,
            })
        else:         
            return render(request, "MealieApp/add_food_form.html",
            {
                "title": "Add New Food",
                "script_src": "MealieApp/js/add_food_form.js",
                "all_food_names": all_food_names,
            })
    else:
        return redirected
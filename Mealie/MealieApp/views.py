import datetime

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

def view_journal_today(request):
    redirected = redirect(request, "auth")
    if not redirected:
        today = datetime.date.today()
        entries = JournalEntry.objects.all()
        for entry in entries:
            print(f"Today is {today} and entry.date is {entry.date}. Do they match? {today==entry.date}")
        if request.method == "POST":
            food_name = request.POST["food-item"]
            print("Requested post item is " + food_name)
            food_item_return = FoodItem.objects.all().filter(name=food_name)
            if food_item_return:
                journal_entry = JournalEntry(
                    date=today,
                    food_item=food_item_return[0],
                    quantity=request.POST["food-quantity"],
                )
                journal_entry.save()
        return view_journal_of(request, today)
    else:
        return redirected

def view_journal_of(request, date):
    redirected = redirect(request, "auth")
    if not redirected:
        # Date is a date object.
        # models.DateField is a match; journal column "date" is a DateField

        entries_qs = JournalEntry.objects.filter(date=date)
        food_names = FoodItem.objects.values("name").order_by("name")
        totals = calculate_totals(entries_qs)
        return render(request, "MealieApp/view_journal_entry.html",
        {
            "title": f"Journal Entry for {str(date)}",
            "date": date,
            "entries_qs": entries_qs,
            "food_names": food_names,
            "totals": totals,
        })
    else:
        return redirected


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

def calculate_totals(entries_queryset):
    totals = {
        "calories": 0,
        "total_fat_dv": 0,
        "saturated_fat_dv": 0,
        "trans_fat_dv": 0,
        "cholesterol_dv": 0,
        "sodium_dv": 0,
        "total_carbohydrates_dv": 0,
        "dietary_fiber_dv": 0,
        "total_sugars": 0,
        "added_sugars_dv": 0,
        "protein": 0,
        "vitamin_d_dv": 0,
        "calcium_dv": 0,
        "iron_dv": 0,
        "potassium_dv": 0,
    }

    for entry in entries_queryset:
        totals["calories"] += entry.food_item.calories * entry.quantity
        totals["total_fat_dv"] += entry.food_item.total_fat_dv
        totals["saturated_fat_dv"] += entry.food_item.saturated_fat_dv
        totals["trans_fat_dv"] += entry.food_item.trans_fat_dv
        totals["cholesterol_dv"] += entry.food_item.cholesterol_dv
        totals["sodium_dv"] += entry.food_item.sodium_dv
        totals["total_carbohydrates_dv"] += entry.food_item.total_carbohydrates_dv
        totals["dietary_fiber_dv"] += entry.food_item.dietary_fiber_dv
        totals["total_sugars"] += entry.food_item.total_sugars
        totals["added_sugars_dv"] += entry.food_item.added_sugars_dv
        totals["protein"] += entry.food_item.protein
        totals["vitamin_d_dv"] += entry.food_item.vitamin_d_dv
        totals["calcium_dv"] += entry.food_item.calcium_dv
        totals["iron_dv"] += entry.food_item.iron_dv
        totals["potassium_dv"] += entry.food_item.potassium_dv * entry.quantity

    return totals

import datetime

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import FoodItem, JournalEntry
from .auth_util import redirect
from .query_util import calculate_totals

from django.db import models

# A separate view file for the experimental route, to isolate imports.

def playground(request):
    redirected = redirect(request, "superuser")
    if not redirected:
        test_qs = FoodItem._meta.get_fields()[2:]
        print(totals)
        return render(request, "MealieApp/experimental/playground.html",
        {
            "title": "Code Playground",
            "test_qs": test_qs,
        })
    else:
        return redirected

def exp_view_journal_entry(request):
    redirected = redirect(request, "superuser")
    if not redirected:
        today = datetime.date.today()
        entries = JournalEntry.objects.all()
        if request.method == "POST":
            food_name = request.POST["food-item"]
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
    redirected = redirect(request, "superuser")
    if not redirected:
        # Date is a date object.
        # models.DateField is a match; journal column "date" is a DateField

        entries_qs = JournalEntry.objects.filter(date=date)
        header_actual_index = 2
        nutritional_index = 4
        table_headers = FoodItem._meta.get_fields()[header_actual_index:]
        nutritional_columns = FoodItem._meta.get_fields()[nutritional_index:]
        food_names = FoodItem.objects.values("name").order_by("name")
        totals = calculate_totals(entries_qs)
        return render(request, "MealieApp/experimental/exp_view_journal_entry.html",
        {
            "title": f"Journal Entry for {str(date)}",
            "date": date,
            "entries_qs": entries_qs,
            "food_names": food_names,
            "table_headers": table_headers,
            "nutritional_columns": nutritional_columns,
            "totals": totals,
            "script_src": "MealieApp/js/experimental/exp_view_food_journal.js",
        })
    else:
        return redirected

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
    redirected = redirect(request, "add")
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
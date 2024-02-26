from django.shortcuts import render
from .models import FoodItem, JournalEntry

# Create your views here.

def index(request):
    return render(request, "MealieApp/index.html",
    {
        "title": "Mealie!",
    })

def view_food_db(request):

    food_db = FoodItem.objects.all()
    return render(request, "MealieApp/view_food_db.html",
    {
        "title": "View Food Database",
        "food_db": food_db,
    })
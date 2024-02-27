from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import FoodItem, JournalEntry

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
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Mealie:login"))
    else:
        food_db = FoodItem.objects.all()
        return render(request, "MealieApp/view_food_db.html",
        {
            "title": "View Food Database",
            "food_db": food_db,
        })
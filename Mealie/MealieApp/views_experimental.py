from django.shortcuts import render
from .models import FoodItem
from .auth_util import redirect


# A separate view file for the experimental route, to isolate imports.

def playground(request):
    redirected = redirect(request, "superuser")
    if not redirected:
        test_qs = FoodItem._meta.get_fields()[2:]
        return render(request, "MealieApp/experimental/playground.html",
        {
            "title": "Code Playground",
            "test_qs": test_qs,
        })
    else:
        return redirected

def view_food_db(request):
    redirected = redirect(request, "auth")
    if not redirected:
        return render(request, "MealieApp/experimental/view_food_db.html",
        {
            "title": "View Food DB",
        })
    else:
        return redirected
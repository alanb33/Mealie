from django.core import serializers
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
        
        header_actual_index = 3
        table_headers = FoodItem._meta.get_fields()[header_actual_index:]

        table_headers_verbose_list = []
        table_headers_list = []
        for header in table_headers:
            table_headers_verbose_list.append(header.verbose_name)
            table_headers_list.append(header.name)

        food_names = serializers.serialize("json", FoodItem.objects.all().order_by("name"))
        
        return render(request, "MealieApp/experimental/view_food_db.html",
        {
            "title": "View Food DB",
            "script_src": "MealieApp/js/experimental/view_food_db.js",
            "food_db_json": food_names,
            "table_headers_verbose": table_headers_verbose_list,
            "table_headers_nonverbose": table_headers_list,
        })
    else:
        return redirected
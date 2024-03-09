from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
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

def del_food(request):
    # NOTE: This code would work in theory, but the design of the journal entry view gets in the way.
    # The journal must be redesigned to do read-only 'pictures' of the values rather than pulling directly from the database.
    redirected = redirect(request, "superuser")
    if not redirected:
        id_to_del = request.GET.get("id")
        if id_to_del:
            try:
                id_to_del = int(id_to_del)
                try:
                    food_item = FoodItem.objects.filter(id=id_to_del).first()
                    food_item.delete()
                    return HttpResponse(f"ID to del: {id_to_del} corresponds with food_item {food_item.name}")
                except IndexError:
                    return HttpResponse("Given ID is invalid.")
            except ValueError:
                return HttpResponse("Given ID is invalid.")
        else:
            return HttpResponse("No ID provided.")
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
            "edit_button_url": reverse("Mealie:index"),
            "delete_button_url": reverse("Mealie:index"),
        })
    else:
        return redirected
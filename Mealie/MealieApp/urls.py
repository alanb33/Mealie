from django.urls import path
from . import views

app_name = "Mealie"
urlpatterns = [
    path("", views.index, name="index"),
    path("debugger/", views.debugger, name="debugger"),
    path("view-food-db/", views.view_food_db, name="view-food-db"),
]
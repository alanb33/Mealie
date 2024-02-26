from django.urls import path
from . import views, views_experimental

app_name = "Mealie"
urlpatterns = [
    path("", views.index, name="index"),
    path("debugger/", views_experimental.debugger, name="debugger"),
    path("view-food-db/", views.view_food_db, name="view-food-db"),
]
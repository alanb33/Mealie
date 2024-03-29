from django.urls import path
from . import views, views_experimental

app_name = "Mealie"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("view-journal-today/", views.view_journal_today, name="view-journal-today"),
    path("view-food-db/", views.view_food_db, name="view-food-db"),
    path("add-food-form/", views.add_food_form, name="add-food-form"),
    path("experimental/playground/", views_experimental.playground, name="experimental/playground"),
    path("experimental/exp-view-journal-entry/", views_experimental.exp_view_journal_entry, name="experimental/exp-view-journal-entry"),
]
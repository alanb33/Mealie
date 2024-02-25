from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "MealieApp/index.html",
    {
        "title": "Mealie!",
    })

def debugger(request):
    return render(request, "Mealieapp/debugger.html",
    {
        "title": "Debugger Page",
    })
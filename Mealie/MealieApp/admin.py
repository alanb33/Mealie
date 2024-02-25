from django.contrib import admin
from .models import FoodItem, JournalEntry

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(JournalEntry)


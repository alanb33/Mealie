from .models import FoodItem

def calculate_totals(entries_queryset):
    totals = {}
    
    actual_header_index = 4
    food_item_headers = FoodItem._meta.get_fields()[actual_header_index:]
    for header in food_item_headers:
        totals[header.name] = 0
        for entry in entries_queryset:
            totals[header.name] += entry.food_item.__getattribute__(header.name) * entry.quantity

    return totals
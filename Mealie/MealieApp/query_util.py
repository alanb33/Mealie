def calculate_totals(entries_queryset):
    totals = {
        "calories": 0,
        "total_fat_dv": 0,
        "saturated_fat_dv": 0,
        "trans_fat_dv": 0,
        "cholesterol_dv": 0,
        "sodium_dv": 0,
        "total_carbohydrates_dv": 0,
        "dietary_fiber_dv": 0,
        "total_sugars": 0,
        "added_sugars_dv": 0,
        "protein": 0,
        "vitamin_d_dv": 0,
        "calcium_dv": 0,
        "iron_dv": 0,
        "potassium_dv": 0,
    }

    for entry in entries_queryset:
        totals["calories"] += entry.food_item.calories * entry.quantity
        totals["total_fat_dv"] += entry.food_item.total_fat_dv * entry.quantity
        totals["saturated_fat_dv"] += entry.food_item.saturated_fat_dv * entry.quantity
        totals["trans_fat_dv"] += entry.food_item.trans_fat_dv * entry.quantity
        totals["cholesterol_dv"] += entry.food_item.cholesterol_dv * entry.quantity
        totals["sodium_dv"] += entry.food_item.sodium_dv * entry.quantity
        totals["total_carbohydrates_dv"] += entry.food_item.total_carbohydrates_dv * entry.quantity
        totals["dietary_fiber_dv"] += entry.food_item.dietary_fiber_dv * entry.quantity
        totals["total_sugars"] += entry.food_item.total_sugars * entry.quantity
        totals["added_sugars_dv"] += entry.food_item.added_sugars_dv * entry.quantity
        totals["protein"] += entry.food_item.protein * entry.quantity
        totals["vitamin_d_dv"] += entry.food_item.vitamin_d_dv * entry.quantity
        totals["calcium_dv"] += entry.food_item.calcium_dv * entry.quantity
        totals["iron_dv"] += entry.food_item.iron_dv * entry.quantity
        totals["potassium_dv"] += entry.food_item.potassium_dv * entry.quantity

    return totals
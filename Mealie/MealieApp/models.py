from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=64)
    serving_size = models.CharField(max_length=64)
    calories = models.IntegerField()
    total_fat_dv = models.IntegerField()
    saturated_fat_dv = models.IntegerField()
    trans_fat = models.IntegerField()
    cholesterol_dv = models.IntegerField()
    sodium_dv = models.IntegerField()
    total_carbohydrates_dv = models.IntegerField()
    dietary_fiber_dv = models.IntegerField()
    total_sugars = models.IntegerField()
    added_sugars_dv = models.IntegerField()
    protein = models.IntegerField()
    vitamin_d_dv = models.IntegerField()
    calcium_dv = models.IntegerField()
    iron_dv = models.IntegerField()
    potassium_dv = models.IntegerField()

class JournalEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    food_item = models.ForeignKey("FoodItem", on_delete=models.PROTECT)
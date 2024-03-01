from django.db import models

class FoodItem(models.Model):
    name = models.CharField("Food Name", max_length=64)
    serving_size = models.CharField("Serving Size", max_length=64)
    calories = models.IntegerField("Calories", default=0)
    total_fat_dv = models.IntegerField("Total Fat (%DV)", default=0)
    saturated_fat_dv = models.IntegerField("Saturated Fat (%DV)", default=0)
    trans_fat_dv = models.IntegerField("Trans Fat (%DV)", default=0)
    cholesterol_dv = models.IntegerField("Cholesterol (%DV)", default=0)
    sodium_dv = models.IntegerField("Sodium (%DV)", default=0)
    total_carbohydrates_dv = models.IntegerField("Total Carbohydrates (%DV)", default=0)
    dietary_fiber_dv = models.IntegerField("Dietary Fiber (%DV)", default=0)
    total_sugars = models.FloatField("Total Sugars", default=0)
    added_sugars_dv = models.IntegerField("Added Sugars (%DV)", default=0)
    protein = models.FloatField("Protein", default=0)
    vitamin_d_dv = models.IntegerField("Vitamin D (%DV)", default=0)
    calcium_dv = models.IntegerField("Calcium (%DV)", default=0)
    iron_dv = models.IntegerField("Iron (%DV)", default=0)
    potassium_dv = models.IntegerField("Potassium (%DV)", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Food Item Entry"
        verbose_name_plural = "Food Item Entries"

class JournalEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    food_item = models.ForeignKey("FoodItem", on_delete=models.PROTECT)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"Journal Entry {str(self.date.today())}: {self.food_item.name} ({self.quantity} servings)"

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"
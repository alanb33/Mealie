# Generated by Django 4.2.10 on 2024-02-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MealieApp", "0004_journalentry_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fooditem",
            name="total_sugars",
            field=models.FloatField(),
        ),
    ]

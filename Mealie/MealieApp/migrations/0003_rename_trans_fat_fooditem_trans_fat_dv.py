# Generated by Django 4.2.10 on 2024-02-29 00:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "MealieApp",
            "0002_alter_fooditem_options_alter_journalentry_options_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="fooditem",
            old_name="trans_fat",
            new_name="trans_fat_dv",
        ),
    ]

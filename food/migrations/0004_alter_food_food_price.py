# Generated by Django 4.2.5 on 2023-10-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0003_alter_food_food_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="food",
            name="food_price",
            field=models.IntegerField(),
        ),
    ]

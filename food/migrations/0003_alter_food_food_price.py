# Generated by Django 4.2.5 on 2023-10-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0002_food_delete_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="food",
            name="food_price",
            field=models.BinaryField(),
        ),
    ]

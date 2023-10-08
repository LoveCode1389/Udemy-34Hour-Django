# Generated by Django 4.2.5 on 2023-10-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("food_name", models.CharField(max_length=200)),
                ("food_desc", models.CharField(max_length=200)),
                ("food_price", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Item",
        ),
    ]
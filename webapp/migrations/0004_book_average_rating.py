# Generated by Django 5.0 on 2023-12-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0003_book_deleted_at_book_is_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="average_rating",
            field=models.FloatField(default=0.0, editable=False),
        ),
    ]
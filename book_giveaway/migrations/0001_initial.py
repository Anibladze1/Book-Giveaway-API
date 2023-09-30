# Generated by Django 4.2.5 on 2023-09-30 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AskForBookRequest",
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
                ("request_date", models.DateTimeField(auto_now_add=True)),
                ("is_confirmed", models.BooleanField(default=False)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="book",
                        to="book.book",
                    ),
                ),
            ],
        ),
    ]

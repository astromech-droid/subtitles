# Generated by Django 4.2.2 on 2023-06-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="title",
            field=models.CharField(max_length=30),
        ),
    ]

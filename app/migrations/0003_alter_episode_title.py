# Generated by Django 4.2.2 on 2023-06-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_episode_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="title",
            field=models.CharField(max_length=35),
        ),
    ]

# Generated by Django 5.0.11 on 2025-02-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]

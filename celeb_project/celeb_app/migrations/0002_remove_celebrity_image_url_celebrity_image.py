# Generated by Django 4.2.5 on 2023-09-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("celeb_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="celebrity",
            name="image_url",
        ),
        migrations.AddField(
            model_name="celebrity",
            name="image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Celebrity",
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
                ("name", models.CharField(max_length=100)),
                ("votes", models.IntegerField(default=0)),
                ("image_url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]

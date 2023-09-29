from django.db import models

class Celebrity(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, default="default.jpg")

    def __str__(self):
        return self.name

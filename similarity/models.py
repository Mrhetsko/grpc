from django.db import models


class Item(models.Model):
    description = models.CharField(max_length=3000)

    def __str__(self):
        return self.description

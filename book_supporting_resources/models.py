from enum import Enum

from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)


class ConditionChoices(Enum):
    NEW = "New"
    USED = "Used"


class Condition(models.Model):
    condition = models.CharField(
        max_length=255,
        choices=[(status.value, status.name) for status in ConditionChoices],
        default=ConditionChoices.NEW.value
    )

    def __str__(self):
        return self.condition
